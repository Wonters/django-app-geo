

class AppSettings:
    def __init__(self, prefix):
        self.prefix = prefix

    def _setting(self, name, dflt):
        """
        Get a setting from django.conf.settings, falling back to the default.
        If the default is not given, uses the setting from django.conf.global_settings.
        """
        from django.conf import settings
        return getattr(settings, self.prefix + name, dflt)
    
    @property
    def GEO_POINTS_MODEL(self):
        """
        The model to use for storing geo points.
        """
        from django.conf import settings
        return getattr(settings, self.prefix + "GEO_POINTS_MODEL", "geo_points.GeoPoint")
