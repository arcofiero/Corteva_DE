from rest_framework import serializers
from .models import WeatherData, WeatherStats

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'

class WeatherStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStats
        fields = '__all__'
