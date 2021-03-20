from django.urls import path, re_path
from . import views

urlpatterns = [path("energy/", views.depEnergy, name="energy department"),

]