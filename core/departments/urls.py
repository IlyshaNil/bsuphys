from django.urls import path, re_path
from . import views


app_name = "departments"
urlpatterns = [path("", views.departmentList, name="energy department"),
    path(
            "/departments/<slug:department>/",
            views.department_detail,
            name="department_detail",
    ),

]