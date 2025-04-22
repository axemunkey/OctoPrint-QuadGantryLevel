# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
from octoprint.util import RepeatedTimer
import flask

class QuadGantryLevelPlugin(octoprint.plugin.StartupPlugin,
                            octoprint.plugin.TemplatePlugin,
                            octoprint.plugin.AssetPlugin,
                            octoprint.plugin.SimpleApiPlugin,
                            octoprint.plugin.SettingsPlugin):

    def __init__(self):
        self._qgl_timer = None

    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        """
        Defines the default settings for the plugin.
        """
        return dict(
            # No specific settings needed for this simple version yet
        )

    ##~~ StartupPlugin mixin

    def on_after_startup(self):
        """
        Called by OctoPrint after the plugin has been initialized.
        """
        self._logger.info("Quad Gantry Level Plugin started!")

    ##~~ AssetPlugin mixin

    def get_assets(self):
        """
        Defines the static assets (JS, CSS) bundled with the plugin.
        """
        return {
            "js": ["js/quadgantrylevel.js"]
            # "css": ["css/quadgantrylevel.css"] # Add if custom styling is needed
        }

    ##~~ TemplatePlugin mixin

    def get_template_configs(self):
        """
        Defines the Jinja2 templates provided by the plugin.
        """
        return [
            dict(type="controls", template="quadgantrylevel_control.jinja2", custom_bindings=True)
        ]

    ##~~ SimpleApiPlugin mixin

    def get_api_commands(self):
        """
        Defines the API commands this plugin supports.
        """
        return dict(
            run_quad_gantry_level=[] # Command name, no parameters expected
        )

    def on_api_command(self, command, data):
        """
        Handles incoming API commands.
        """
        if command == "run_quad_gantry_level":
            if not self._printer.is_operational() or self._printer.is_printing():
                self._logger.warning("Printer not operational or is printing, cannot run QUAD_GANTRY_LEVEL.")
                return flask.make_response("Printer not ready", 409) # Conflict status code

            self._logger.info("Sending QUAD_GANTRY_LEVEL command.")
            self._printer.commands("QUAD_GANTRY_LEVEL")
            return flask.make_response("Command sent", 200)

    ##~~ Softwareupdate hook

    def get_update_information(self):
        """
        Defines how OctoPrint checks for plugin updates.
        """
        # Default repository name, can be changed in setup.py
        repo_name = "OctoPrint-QuadGantryLevel"
        # Attempt to load plugin_info if available (set during packaging)
        if hasattr(self, "_plugin_info") and self._plugin_info is not None:
             if "github_repo" in self._plugin_info:
                 repo_name = self._plugin_info["github_repo"]

        return dict(
            quadgantrylevel=dict(
                displayName="Quad Gantry Level Plugin",
                displayVersion=self._plugin_version,

                # Check against the plugin's repository for new versions
                type="github_release",
                user="axemunkey", # Replaced placeholder
                repo=repo_name, # Use variable for repo name
                current=self._plugin_version,

                # Update method: pip
                pip="https://github.com/{user}/{repo}/archive/{target_version}.zip"
            )
        )

# Associate the plugin with OctoPrint's plugin system
__plugin_name__ = "Quad Gantry Level"
__plugin_pythoncompat__ = ">=3.7,<4" # Adjust Python compatibility as needed

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = QuadGantryLevelPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
