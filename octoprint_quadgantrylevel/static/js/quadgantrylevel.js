/*
 * View model for OctoPrint-QuadGantryLevel
 *
 * Author: Your Name
 * License: AGPLv3
 */
$(function() {
    function QuadgantrylevelViewModel(parameters) {
        var self = this;

        // Assign dependencies injected by OctoPrint
        self.loginState = parameters[0];
        self.settings = parameters[1]; // If you need settings later
        self.printerState = parameters[2];

        // --- View Model Functions ---

        /**
         * Sends the API command to the Python backend to trigger QUAD_GANTRY_LEVEL.
         */
        self.runQuadGantryLevel = function() {
            // Check again just before sending, although button enable state should prevent this
            if (!self.printerState.isOperational() || self.printerState.isPrinting()) {
                console.warn("QuadGantryLevel: Printer not ready, command blocked by UI.");
                // Optionally show a notification
                // new PNotify({ title: 'Printer Not Ready', text: 'Cannot run Quad Gantry Level while printer is not operational or printing.', type: 'warning', hide: true });
                return;
            }

            console.log("QuadGantryLevel: Sending run_quad_gantry_level command...");

            // Use OctoPrint's simple API command helper
            OctoPrint.simpleApiCommand("quadgantrylevel", "run_quad_gantry_level", {})
                .done(function(response) {
                    console.log("QuadGantryLevel: Command sent successfully.", response);
                    // Optionally show success notification
                    // new PNotify({ title: 'Command Sent', text: 'QUAD_GANTRY_LEVEL command sent to printer.', type: 'success', hide: true });
                })
                .fail(function(jqXHR, textStatus, errorThrown) {
                    console.error("QuadGantryLevel: Failed to send command.", textStatus, errorThrown, jqXHR.responseText);
                    // Show error notification
                    new PNotify({
                        title: 'Command Failed',
                        text: 'Failed to send QUAD_GANTRY_LEVEL command. Check OctoPrint logs. Reason: ' + (jqXHR.responseText || errorThrown),
                        type: 'error',
                        hide: false // Keep error visible until dismissed
                    });
                });
        };

        // --- OctoPrint Hooks ---

        /*
        // Example: If you needed to bind this view model to a specific element
        self.onBeforeBinding = function() {
            // Initialization logic before Knockout bindings are applied
        }

        // Example: If you needed access to settings
        self.onSettingsShown = function() {
            // Logic when the plugin's settings dialog is shown
        }
        */
    }

    // Register the view model with OctoPrint
    // Dependencies are injected into the constructor in the order specified here
    OCTOPRINT_VIEWMODELS.push({
        construct: QuadgantrylevelViewModel,
        // ViewModels your plugin depends on, e.g. loginStateViewModel, settingsViewModel, printerStateViewModel
        dependencies: [ "loginStateViewModel", "settingsViewModel", "printerStateViewModel" ],
        // Elements to bind to, e.g. ["#settings_plugin_quadgantrylevel", "#navbar_plugin_quadgantrylevel"]
        elements: [ "#quadgantrylevel_control_button" ] // Bind to the div containing our button
    });
});
