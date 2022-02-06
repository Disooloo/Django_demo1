
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('blogs', include('blogs.urls')),
    path('weather', include('weather.urls')),

]
