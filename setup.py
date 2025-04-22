# coding=utf-8
import setuptools

# The plugin's identifier, has to be unique
plugin_identifier = "quadgantrylevel"

# The plugin's python package, should be unique like the identifier
plugin_package = "octoprint_quadgantrylevel"

# The plugin's human readable name. Can be overwritten within OctoPrint's internal data via __plugin_name__ in the plugin module
plugin_name = "OctoPrint-QuadGantryLevel" # You might want to change this if the repo name changes

# The plugin's version. Can be overwritten within OctoPrint's internal data via __plugin_version__ in the plugin module
plugin_version = "0.1.0"

# The plugin's description. Can be overwritten within OctoPrint's internal data via __plugin_description__ in the plugin module
plugin_description = """Adds a button to the Control tab to run QUAD_GANTRY_LEVEL."""

# The plugin's author. Can be overwritten within OctoPrint's internal data via __plugin_author__ in the plugin module
plugin_author = "Nicholas Rothgeb" # Replaced placeholder

# The plugin's author's email address.
plugin_author_email = "nicholas.rothgeb@gmail.com" # Replaced placeholder

# The plugin's homepage URL. Can be overwritten within OctoPrint's internal data via __plugin_url__ in the plugin module
# Ensure this matches the repository name used in __init__.py get_update_information
plugin_repo_name = "OctoPrint-QuadGantryLevel" # Define repo name here
plugin_url = f"https://github.com/axemunkey/{plugin_repo_name}" # Replaced placeholder and used repo name

# The plugin's license. Can be overwritten within OctoPrint's internal data via __plugin_license__ in the plugin module
plugin_license = "CC BY-NC-SA 4.0" # Updated license to Creative Commons BY-NC-SA 4.0

# Any additional requirements besides OctoPrint should be listed here
plugin_requires = []

# Additional package data to install
plugin_additional_data = []

# Link to the plugin implementation module folder
plugin_namespace = "octoprint_quadgantrylevel"

# Path to the plugin implementation module file
plugin_entry_point = "octoprint_quadgantrylevel:__plugin_load__"

# Additional setup arguments, e.g. list of requires
# See https://github.com/OctoPrint/OctoPrint/wiki/Plugin:-Packaging#providing-additional-data-files
# and https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/
# for details
setup_requires = []
install_requires = plugin_requires
extras_require = {}

try:
    import octoprint_setuptools
except ImportError:
    print(
        "Could not import OctoPrint's setuptools, are you sure you are running that under "
        "the same python installation that OctoPrint is installed under?"
    )
    import sys
    sys.exit(-1)

# Pass the GitHub repository name to the plugin implementation
plugin_info = {
    "github_repo": plugin_repo_name
}

# Note: Standard PyPI classifiers don't include CC BY-NC-SA 4.0.
# If distributing via PyPI, you might need to use a generic classifier
# like 'License :: Other/Proprietary License' and rely on the README/LICENSE file.
# However, for OctoPrint's plugin repository, specifying the string is usually sufficient.
setup_kwargs = octoprint_setuptools.create_plugin_setup_kwargs(
    identifier=plugin_identifier,
    package=plugin_package,
    name=plugin_name,
    version=plugin_version,
    description=plugin_description,
    author=plugin_author,
    mail=plugin_author_email,
    url=plugin_url,
    license=plugin_license, # Pass the updated license string
    requires=plugin_requires,
    additional_data=plugin_additional_data,
    namespace=plugin_namespace,
    entry_point=plugin_entry_point,
    setup_requires=setup_requires,
    install_requires=install_requires,
    extras_require=extras_require,
    plugin_info=plugin_info # Pass additional info
)

setuptools.setup(**setup_kwargs)
