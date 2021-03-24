from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Department
from home.models import MainPageStatisticNumber, KeyPublications, FamousGraduates
from django.utils import timezone
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.conf import settings
from django.http import HttpResponse
from django.utils import translation
from django.db.models import Max
import random

# Create your views here.
def departmentList(request):
    return render(request, "DepartmentList.html")


def department_detail(request, department):
    department = get_object_or_404(
        Department,
        slug=department,

    )
    return render(request, "departmentMain.html", {"dep": department})


def department_detail_thesis(request, department):
    department = get_object_or_404(
        Department,
        slug=department,

    )
    return render(request, "depInf2.html", {"dep": department})


def department_detail_directions(request, department):
    department = get_object_or_404(
        Department,
        slug=department,

    )
    return render(request, "depInf.html", {"dep": department})