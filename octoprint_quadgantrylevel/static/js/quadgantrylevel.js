/*
 * View model for OctoPrint-QuadGantryLevel
 *
 * Author: Nicholas Rothgeb
 * License: CC BY-NC-SA 4.0
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
                // Show a notification using PNotify (OctoPrint's notification library)
                new PNotify({ title: 'Printer Not Ready', text: 'Cannot run Gantry Level while printer is not operational or printing.', type: 'warning', hide: true, delay: 3000 });
                return;
            }

            console.log("QuadGantryLevel: Sending run_quad_gantry_level command...");

            // Use OctoPrint's simple API command helper
            OctoPrint.simpleApiCommand("quadgantrylevel", "run_quad_gantry_level", {})
                .done(function(response) {
                    console.log("QuadGantryLevel: Command sent successfully.", response);
                    // Show success notification
                    new PNotify({ title: 'Command Sent', text: 'QUAD_GANTRY_LEVEL command sent to printer.', type: 'success', hide: true, delay: 3000 });
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

        /**
         * Called by OctoPrint after the main UI bindings have been applied.
         * We use this hook to manually inject our button HTML into the DOM
         * and then apply Knockout bindings specifically to our injected element.
         */
        self.onAfterBinding = function() {
            console.log("QuadGantryLevel: onAfterBinding called. Attempting to inject button.");

            // Define the HTML structure for our button panel
            // Note: Using $data context for bindings as we apply bindings specifically to this node.
            var buttonHtml = `
                <div id="quadgantrylevel_control_button" class="jog-panel">
                    <h4>Quad Gantry Level</h4>
                    <button class="btn btn-block"
                            data-bind="click: $data.runQuadGantryLevel,
                                       enable: $data.loginState.isUser() && $data.printerState.isOperational() && !$data.printerState.isPrinting()">
                        <i class="fas fa-balance-scale-right"></i>
                        Gantry Level
                    </button>
                </div>
            `;

            // Select the target element on the Control tab to insert our panel after.
            // #control-jog-general is the div containing the 'Motors Off', 'Fan On/Off' buttons.
            var targetElement = $("#control-jog-general");

            if (targetElement.length) {
                // If the target element exists, insert our HTML after it.
                targetElement.after(buttonHtml);
                console.log("QuadGantryLevel: Button HTML injected after #control-jog-general.");

                // Get a reference to the DOM element we just inserted.
                var insertedElement = document.getElementById('quadgantrylevel_control_button');

                if (insertedElement) {
                    // Apply Knockout bindings specifically to our new element.
                    // Pass the view model (self) and the element node.
                    ko.applyBindings(self, insertedElement); // <-- Simplified this call
                    console.log("QuadGantryLevel: Knockout bindings applied to #quadgantrylevel_control_button.");
                } else {
                     console.error("QuadGantryLevel: CRITICAL - Failed to find #quadgantrylevel_control_button immediately after injection.");
                }
            } else {
                console.error("QuadGantryLevel: Could not find target element '#control-jog-general' to insert button after. Button not added.");
            }
        };
    }

    /* OCTOPRINT VIEWMODELS */
    OCTOPRINT_VIEWMODELS.push({
        construct: QuadgantrylevelViewModel,
        dependencies: [
            "loginStateViewModel",
            "settingsViewModel",
            "printerStateViewModel"
        ],
        // No 'elements' array needed here
    });
});
