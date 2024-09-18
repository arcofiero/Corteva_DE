from rest_framework import generics
from .models import WeatherData, WeatherStats
from .serializers import WeatherDataSerializer, WeatherStatsSerializer
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import WeatherData, WeatherStats
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


def paginate_query(request, queryset):
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 25)  # Show 25 records per page
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    
    return results


class WeatherDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['station', 'date']

    # Use 'list' for collection GET requests
    def weather_list(self, request, *args, **kwargs):
        date = request.GET.get('date')
        station = request.GET.get('station')
        queryset = self.get_queryset()

        if date:
            queryset = queryset.filter(date=date)
        if station:
            queryset = queryset.filter(station=station)
        
        queryset = paginate_query(request, queryset)
        
        data = [{"date": str(item.date), "max_temp": item.max_temp, "min_temp": item.min_temp, "precipitation": item.precipitation} for item in queryset]
        return JsonResponse(data, safe=False)


class WeatherStatsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WeatherStats.objects.all()
    serializer_class = WeatherStatsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['station', 'year']  # 'year' instead of 'date'

    def weather_stats(self, request, *args, **kwargs):
        date = request.GET.get('date')
        station = request.GET.get('station')
        queryset = self.get_queryset()

        if date:
            # Assuming you want to filter by year, extracting the year from the date.
            year = date.split("-")[0]  # Get year part from 'YYYY-MM-DD'
            queryset = queryset.filter(year=year)
        if station:
            queryset = queryset.filter(station=station)

        queryset = paginate_query(request, queryset)
        
        data = [{"year": item.year, "station": item.station, "avg_max_temp": item.avg_max_temp, "avg_min_temp": item.avg_min_temp, "total_precipitation": item.total_precipitation} for item in queryset]
        return JsonResponse(data, safe=False)


