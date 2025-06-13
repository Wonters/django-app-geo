from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Peak(models.Model):
    lat = models.DecimalField(default=1, decimal_places=7, max_digits=10,
                              validators=[MaxValueValidator(90), MinValueValidator(-90)])
    lon = models.DecimalField(default=1, decimal_places=7, max_digits=10,
                              validators=[MaxValueValidator(180), MinValueValidator(-180)])
    altitude = models.IntegerField(default=1)
    name = models.CharField(default='', max_length=100)
    message_meteo = models.CharField(default='', max_length=300)

    def __str__(self):
        return f"{self.name}:{self.altitude_km()}:{self.message_meteo}"

    def get_geo_bb(self):
        return [str(self.lat), str(self.lon)]

    def altitude_km(self):
        return self.altitude/1000

class IPRejected(models.Model):
    ip = models.GenericIPAddressField()