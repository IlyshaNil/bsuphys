from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="index"),
               path("template/", views.templates, name="index"),
                path("dekanat/", views.dekanat, name="index"),
                path("spec/", views.spec, name="spec"),
               ]
