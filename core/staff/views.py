from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Staff_unit


def staff_detail(request, staff):
    staff = get_object_or_404(Staff_unit, slug=staff,)
    return render(request, "personTemplate.html", {"staff": staff})