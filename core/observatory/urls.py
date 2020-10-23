from django.urls import path, re_path
from . import views

urlpatterns = [path("", views.observatoryMain, name="observatoryMain"),
               path("employee/", views.observatoryEmployee, name="observatoryMain"),
               path("equipment/", views.observatoryEquipment, name="observatoryMain"),

               path("contacts/", views.observatoryContacts, name="observatoryMain"),
                path("science-pop/", views.observatoryPopular, name="observatoryMain"),
                path("science-pop/lections/", views.observatoryPopular, name="observatoryMain"),
]