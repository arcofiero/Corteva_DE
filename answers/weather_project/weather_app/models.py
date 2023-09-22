from django.db import models

class WeatherData(models.Model):
    station = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    max_temp = models.IntegerField(blank=True, null=True)
    min_temp = models.IntegerField(blank=True, null=True)
    precipitation = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_data'

class WeatherStats(models.Model):
    station = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    avg_max_temp = models.FloatField(blank=True, null=True)
    avg_min_temp = models.FloatField(blank=True, null=True)
    total_precipitation = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_stats'

