from django.test import TestCase
from .models import WeatherData

class WeatherDataTestCase(TestCase):
    def setUp(self):
        WeatherData.objects.create(station="test_station", date="2022-01-01", max_temp=23.5, min_temp=10.2, precipitation=5)

    def test_weather_data_exists(self):
        """WeatherData objects are saved and retrievable"""
        test_station = WeatherData.objects.get(station="test_station")
        self.assertEqual(test_station.max_temp, 23.5)

    