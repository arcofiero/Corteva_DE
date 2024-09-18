from django.db import models

class WeatherData(models.Model):
    station = models.CharField(max_length=100)
    date = models.DateField()
    max_temp = models.FloatField()  # Use DecimalField if needed
    min_temp = models.FloatField()
    precipitation = models.FloatField()


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

