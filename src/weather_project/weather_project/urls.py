# """
# URL configuration for weather_project project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.urls import path, include
from weather_app import views  # Import the views from weather_app
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Weather API",
      default_version='v1',
      description="Weather API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.home, name='home'),  # Link the root URL to the home view
    path('api/weather/', views.WeatherDataViewSet.as_view({'get': 'weather_list'}), name='weather'),
    path('api/weather/stats/', views.WeatherStatsViewSet.as_view({'get': 'weather_stats'}), name='weather_stats'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
from django.urls import path, include
from weather_app import views  # Import the views from weather_app
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Weather API",
      default_version='v1',
      description="Weather API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.home, name='home'),  # Link the root URL to the home view
    path('api/weather/', views.WeatherDataViewSet.as_view({'get': 'weather_list'}), name='weather'),
    path('api/weather/stats/', views.WeatherStatsViewSet.as_view({'get': 'weather_stats'}), name='weather_stats'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
