from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from home.models import MainPageStatisticNumber, KeyPublications, FamousGraduates
from django.utils import timezone
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.conf import settings
from django.http import HttpResponse
from django.utils import translation
from django.db.models import Max
import random

# Create your views here.
def depEnergy(request):
    return render(request, "departmentMain.html")