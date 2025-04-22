# coding=utf-8
import setuptools
import os

# The plugin's identifier, has to be unique
plugin_identifier = "quadgantrylevel"

# The plugin's python package, should be unique like the identifier
plugin_package = "octoprint_quadgantrylevel"

# The plugin's human readable name. Can be overwritten within OctoPrint's internal data via __plugin_name__ in the plugin module
plugin_name = "OctoPrint-QuadGantryLevel"

# The plugin's version. Can be overwritten within OctoPrint's internal data via __plugin_version__ in the plugin module
plugin_version = "0.1.1" # Incremented version number for the update

# The plugin's description. Can be overwritten within OctoPrint's internal data via __plugin_description__ in the plugin module
plugin_description = """Adds a button to the Control tab to run QUAD_GANTRY_LEVEL."""

# The plugin's author. Can be overwritten within OctoPrint's internal data via __plugin_author__ in the plugin module
plugin_author = "Nicholas Rothgeb"

# The plugin's author's email address.
plugin_author_email = "nicholas.rothgeb@gmail.com"

# The plugin's homepage URL. Can be overwritten within OctoPrint's internal data via __plugin_url__ in the plugin module
plugin_repo_name = "OctoPrint-QuadGantryLevel"
plugin_url = f"https://github.com/axemunkey/{plugin_repo_name}"

# The plugin's license. Can be overwritten within OctoPrint's internal data via __plugin_license__ in the plugin module
plugin_license = "CC BY-NC-SA 4.0"

# Any additional requirements besides OctoPrint should be listed here
plugin_requires = []

# Link to the plugin implementation module folder
plugin_namespace = "octoprint_quadgantrylevel"

# Path to the plugin implementation module file
plugin_entry_point = "octoprint_quadgantrylevel:__plugin_load__"

# Find packages automatically
packages = setuptools.find_packages(exclude=("tests", "tests.*"))

# Define the setup arguments directly
setup_kwargs = {
    "name": plugin_name,
    "version": plugin_version,
    "description": plugin_description,
    "long_description": plugin_description, # Often same as description for simple plugins
    "author": plugin_author,
    "author_email": plugin_author_email,
    "url": plugin_url,
    "license": plugin_license,
    "packages": packages,
    "include_package_data": True, # Tells setuptools to use MANIFEST.in
    # "package_data": plugin_package_data, # Removed this line - rely on MANIFEST.in
    "install_requires": plugin_requires,
    "entry_points": {
        # Define the entry point for OctoPrint plugin loading
        "octoprint.plugin": [
            f"{plugin_identifier} = {plugin_entry_point}"
        ]
    },
    "python_requires": ">=3.7,<4", # Match python compat from __init__.py
}

# Check if octoprint_setuptools is available, just in case, but don't rely on the newer function
try:
    import octoprint_setuptools
except ImportError:
    print(
        "Could not import OctoPrint's setuptools, are you sure you are running that under "
        "the same python installation that OctoPrint is installed under?"
    )
    pass # Proceed even if not found, basic setuptools might work

# Perform the setup
setuptools.setup(**setup_kwargs)
