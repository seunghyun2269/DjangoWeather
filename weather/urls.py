
from django.contrib import admin
from django.urls import path
from page import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = "home"),
    path('weather/', views.weather, name = "weather"),
    path('error/', views.error, name = "error")
]
