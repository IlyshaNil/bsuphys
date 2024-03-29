from django.urls import path
from . import views

app_name = "quantum_School"
urlpatterns = [
    path("", views.quantumMain, name="quantum"),
    path("quantum-uni/", views.quantumUni, name="quantum"),
    path("quantum-9/", views.quantumNine, name="quantum"),
    path("quantum-10/", views.quantumTen, name="quantum"),
    path("quantum-11/", views.quantumEleven, name="quantum"),
    path("quantum-olimp/", views.quantumOlimp, name="quantum"),
    path("quantum-uni/ads", views.quantumAdvertisement, name="quantum"),
    path("quantum-9/ads", views.quantumAdvertisement, name="quantum"),
    path("quantum-10/ads", views.quantumAdvertisement, name="quantum"),
    path("quantum-11/ads", views.quantumAdvertisement, name="quantum"),
    path("quantum-olimp/ads", views.quantumAdvertisement, name="quantum"),
    path("quantum-olimp/urls/", views.quantumUrls, name="quantum"),
    path("all-quantum-lessons-schedule/", views.schedule, name="quantum"),
]
