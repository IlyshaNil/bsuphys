from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Staff_unit
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag


# Create your views here.
def staff_detail(request, staff):
    staff = get_object_or_404(
        Staff_unit,
        slug=staff,

    )
    return render(request, "personTemplate.html", {"staff": staff})


def staff_list(request):
    object_list = Staff_unit.objects.all()
    return render(request, "listStaffTemplate.html", {"staff": object_list},)