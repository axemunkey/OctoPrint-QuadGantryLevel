# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import flask # Ensure flask is imported

# Removed: from octoprint.util import RepeatedTimer (not used)


# Removed TemplatePlugin from the list of inherited classes
class QuadGantryLevelPlugin(octoprint.plugin.StartupPlugin,
                            octoprint.plugin.AssetPlugin,
                            octoprint.plugin.SimpleApiPlugin,
                            octoprint.plugin.SettingsPlugin):

    def __init__(self):
        pass

    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        """
        Defines the default settings for the plugin.
        """
        return dict()

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
        # Ensure the JS file is still included
        return {
            "js": ["js/quadgantrylevel.js"]
        }

    ##~~ TemplatePlugin mixin - REMOVED ~~##

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
                # Return a conflict response (this is fine as text)
                return flask.make_response("Printer not ready", 409)

            self._logger.info("Sending QUAD_GANTRY_LEVEL command.")
            # Send the G-code command to the printer
            self._printer.commands("QUAD_GANTRY_LEVEL")

            # *** FIX: Return an empty JSON object on success ***
            return flask.jsonify({}) # Changed from make_response("Command sent", 200)

        # Return not found if the command is unknown
        return flask.make_response("Unknown command", 404)


    ##~~ Softwareupdate hook

    def get_update_information(self):
        """
        Defines how OctoPrint checks for plugin updates.
        """
        # Define the update check configuration directly.
        repo_name = "OctoPrint-QuadGantryLevel"
        github_user = "axemunkey"

        return {
            "quadgantrylevel": {
                "displayName": "Quad Gantry Level Plugin",
                "displayVersion": self._plugin_version,
                "type": "github_release",
                "user": github_user,
                "repo": repo_name,
                "current": self._plugin_version,
                "pip": f"https://github.com/{github_user}/{repo_name}/archive/{{target_version}}.zip",
            }
        }

# Associate the plugin with OctoPrint's plugin system
__plugin_name__ = "Quad Gantry Level"
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
