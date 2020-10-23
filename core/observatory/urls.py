from django.urls import path, re_path
from . import views

urlpatterns = [path("", views.observatoryMain, name="observatoryMain"),
               path("employee/", views.observatoryEmployee, name="observatoryMain"),
]