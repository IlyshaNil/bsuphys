from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.observatoryMain, name="observatoryMain"),
    path("employee/", views.observatoryEmployee, name="observatoryMain"),
    path("equipment/", views.observatoryEquipment, name="observatoryMain"),
    path("science-dir/", views.observatoryScienceDirections, name="observatoryMain"),
    path(
        "edu-activity/", views.observatoryEducationalActivities, name="observatoryMain"
    ),
    path("contacts/", views.observatoryContacts, name="observatoryMain"),
    path("science-res/", views.observatoryScienceResults, name="observatoryMain"),
    path("science-pop/", views.observatoryPopular, name="observatoryMain"),
    path(
        "science-pop/lections/",
        views.observatoryPopularLections,
        name="observatoryMain",
    ),
    path("science-pop/miff/", views.observatoryPopularMIFF, name="observatoryMain"),
    path("publications/", views.observatoryPublications, name="observatoryMain"),
    path(
        "publications/articles/",
        views.observatoryPublicationsArticle,
        name="observatoryMain",
    ),
    path(
        "publications/books/",
        views.observatoryPublicationsBooks,
        name="observatoryMain",
    ),
    path(
        "publications/conferences/",
        views.observatoryPublicationsConference,
        name="observatoryMain",
    ),
    path(
        "publications/encyclopedia/",
        views.observatoryPublicationsWiki,
        name="observatoryMain",
    ),
]
