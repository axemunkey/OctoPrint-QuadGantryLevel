# OctoPrint-QuadGantryLevel Plugin

A simple OctoPrint plugin that adds a button to the Control tab to trigger the `QUAD_GANTRY_LEVEL` G-code command, commonly used with Klipper firmware for printers with multiple Z-axis steppers.

## Features

* Adds a "Gantry Level" button directly to the OctoPrint Control tab.
* Button is only enabled when the printer is operational and not printing, preventing accidental activation.
* Sends the `QUAD_GANTRY_LEVEL` command to the printer when clicked.

## Screenshot

*(Imagine a screenshot here showing the OctoPrint Control tab with the "Gantry Level" button highlighted)*

## Setup

Install via the bundled Plugin Manager or manually using this URL:

https://github.com/axemunkey/OctoPrint-QuadGantryLevel/archive/main.zip
Alternatively, you can install manually from the command line:

1.  SSH into your OctoPrint server (e.g., OctoPi).
2.  Activate the Python virtual environment where OctoPrint is installed:
    ```bash
    source ~/oprint/bin/activate
    ```
    *(Note: The path `~/oprint/` might differ based on your setup)*
3.  Install the plugin from the cloned repository or downloaded source:
    ```bash
    # Option 1: Clone the repository
    # git clone [https://github.com/axemunkey/OctoPrint-QuadGantryLevel.git](https://github.com/axemunkey/OctoPrint-QuadGantryLevel.git)
    # cd OctoPrint-QuadGantryLevel
    # pip install .

    # Option 2: Install directly from GitHub URL (replace 'main' with a specific tag/release if needed)
    pip install "[https://github.com/axemunkey/OctoPrint-QuadGantryLevel/archive/main.zip](https://github.com/axemunkey/OctoPrint-QuadGantryLevel/archive/main.zip)"
    ```
4.  Restart the OctoPrint server:
    ```bash
    sudo service octoprint restart
    ```

## Configuration

This plugin currently requires no configuration. The button will appear on the Control tab after installation and server restart.

## Author

Created and maintained by Nicholas Rothgeb ([@axemunkey](https://github.com/axemunkey)).

## License

This plugin is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).

You are free to:
* **Share** — copy and redistribute the material in any medium or format
* **Adapt** — remix, transform, and build upon the material

Under the following terms:
* **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
* **NonCommercial** — You may not use the material for commercial purposes.
* **ShareAlike** — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

See the [full license text](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) for details. You should include a copy of the license text (or a link to it) in your repository (e.g., in a `LICENSE` file).
