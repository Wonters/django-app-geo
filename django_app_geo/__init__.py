"""
Django App Geo - Geographic point handling app
"""

VERSION = (0, 1, 0, "final", 0)
__title__ = "django_app_geo"
__version_info__ = VERSION
__version__ = ".".join(map(str, VERSION[:3])) + (
    "-{}{}".format(VERSION[3], VERSION[4] or "") if VERSION[3] != "final" else ""
)
__author__ = "Shift Team"
__email__ = "shift.python.software@gmail.com"
__license__ = "MIT"
__copyright__ = "Copyright 2025 Shift Team"

# Don't import Django models here to avoid AppRegistryNotReady error
# Models will be available when Django is properly initialized