from django.urls import path, re_path
from . import views

urlpatterns = [path("", views.index, name="index"),
               path("template/", views.templates, name="index"),
               path("dekanat/", views.dekanat, name="index"),
               path("spec/", views.spec, name="specialization"),

               path("abitur/", views.abitur, name="abitur"),
               path("info/", views.info, name="info"),

               path("faculty/", views.faculty, name="faculty"),
               path("enter/", views.enter, name="enter"),
               path("cooperation/", views.cooperation, name="cooperation"),
               path("science/", views.science, name="science"),
               path("education/", views.education, name="education"),
               path("contacts/", views.contacts, name="contacts"),
               path("departments/", views.departments, name="departments"),
               path("council/", views.council, name="council"),
               path("one-window/", views.oneWindow, name="one window"),
               path("map/", views.mapApi, name="map"),
               path("faculty/documents/", views.NwordDocuments, name="documents"),
               path("worldwide", views.internationalConnection, name="international"),

               re_path(r'.+/language_en', views.language_switch_en, name="language_en"),
               re_path(r'.+/language_ru', views.language_switch_ru, name="language_ru"),
               path("en_main/", views.language_switch_en_main, name="lang_en_main"),
               path("ru_main/", views.language_switch_ru_main, name="lang_ru_main"),

               path("time/", views.timetable, name="info"),

                path("mezzija/", views.timofey, name="info"),

               ]
