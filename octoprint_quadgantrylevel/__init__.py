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
        # No timer needed for this simple version
        pass

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
            # Define the template for the control tab section
            dict(type="controls", template="quadgantrylevel_control.jinja2", custom_bindings=True)
            # Example for settings:
            # dict(type="settings", template="quadgantrylevel_settings.jinja2", custom_bindings=False)
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
            # Check printer state before sending command
            if not self._printer.is_operational() or self._printer.is_printing():
                self._logger.warning("Printer not operational or is printing, cannot run QUAD_GANTRY_LEVEL.")
                # Return a conflict response
                return flask.make_response("Printer not ready", 409)

            self._logger.info("Sending QUAD_GANTRY_LEVEL command.")
            # Send the G-code command to the printer
            self._printer.commands("QUAD_GANTRY_LEVEL")
            # Return a success response
            return flask.make_response("Command sent", 200)

        # Return not found if the command is unknown
        return flask.make_response("Unknown command", 404)


    ##~~ Softwareupdate hook

    def get_update_information(self):
        """
        Defines how OctoPrint checks for plugin updates.
        """
        # Define the update check configuration directly.
        # !! Replace "OctoPrint-QuadGantryLevel" if your repo name is different !!
        repo_name = "OctoPrint-QuadGantryLevel"
        github_user = "axemunkey"

        return {
            # Plugin identifier (must match setup.py and registration)
            "quadgantrylevel": {
                "displayName": "Quad Gantry Level Plugin",
                "displayVersion": self._plugin_version,

                # Type of update mechanism
                "type": "github_release",

                # GitHub repository details
                "user": github_user,
                "repo": repo_name,

                # Current version of the plugin
                "current": self._plugin_version,

                # Update method: pip install from github release zip
                "pip": f"https://github.com/{github_user}/{repo_name}/archive/{{target_version}}.zip",

                # Optionally, you can specify tags/branches to check
                # "tags": True, # Check tags instead of releases
                # "branches": "main", # Check a specific branch
            }
        }

# Associate the plugin with OctoPrint's plugin system
# Plugin Name (can be overridden by __plugin_name__ in __init__.py)
__plugin_name__ = "Quad Gantry Level"
# Python Compatibility (important for OctoPrint >= 1.4.0)
__plugin_pythoncompat__ = ">=3.7,<4"

def __plugin_load__():
    """
    Loads the plugin, registers implementations, and hooks.
    """
    global __plugin_implementation__
    __plugin_implementation__ = QuadGantryLevelPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        # Register the software update information hook
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
