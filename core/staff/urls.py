from django.urls import path
from . import views


app_name = "staff"
urlpatterns = [
    #path("list/", views.weAreInMedia, name="post_list"),
    path(
        "<slug:staff>/",
        views.staff_detail,
        name="staff_detail",
    ),
]