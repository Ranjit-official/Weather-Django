from django.db import models
# id
# city
# country
# latitude
# logintude
# temperature
# weather_desciption
# humidity
# wind_speed
# Create your models here.
class Temperature(models.Model):
    city = models.CharField(max_length=100,)
    country = models.CharField(max_length=100)
    latitude = models.CharField(max_length=500)
    logintude = models.CharField(max_length=100)
    weather_description = models.CharField(max_length=100)
    humitidy = models.CharField(max_length=100)
    temperature =models.CharField(max_length=5)

    def __str__(self):
        return self.city;