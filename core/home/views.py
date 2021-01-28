from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from home.models import MainPageStatisticNumber
from django.utils import timezone
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.conf import settings
from django.http import HttpResponse
from django.utils import translation
from django.db.models import Max
import random


def language_switch_en(request):
    user_language = 'en'
    translation.activate(user_language)
    response = HttpResponse(status=302)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)

    refresh_path = request.path[:request.path.find("/language_en")]


    refresh_path = refresh_path.replace('/ru/', '/en/')
    response['Location'] = refresh_path
    return response

def language_switch_ru(request):
    user_language = 'ru'
    translation.activate(user_language)
    response = HttpResponse(status=302)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)

    refresh_path = request.path[:request.path.find("/language_ru")]
    refresh_path = refresh_path.replace('/en/', '/ru/')
    response['Location'] = refresh_path
    return response

def language_switch_en_main(request):
    user_language = 'en'
    translation.activate(user_language)
    response = HttpResponse(status=302)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    response['Location'] = "/"
    return response

def language_switch_ru_main(request):
    user_language = 'ru'
    translation.activate(user_language)
    response = HttpResponse(status=302)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    response['Location'] = "/"
    return response


def index(request):
    post = Post.published.latest("publish")
    randomNumbers = get_random_statistic_number()
    return render(request, "main.html", {"post": post,
                                         "stat1": randomNumbers[0],
                                         "stat2": randomNumbers[1],
                                         "stat3": randomNumbers[2],
                                         "stat4": randomNumbers[3],
                                         "stat5": randomNumbers[4]})


def templates(request):
    posts = Post.published.latest("publish")
    return render(request, "template1.html", {"posts": posts})


def dekanat(request):
    return render(request, "dekanat.html")


def spec(request):
    return render(request, "spex.html")


def abitur(request):
    return render(request, "enrollee.html")


def info(request):
    return render(request, "mainInf.html")


def faculty(request):
    return render(request, "1.html")


def enter(request):
    return render(request, "2.html")


def cooperation(request):
    return render(request, "3.html")


def science(request):
    return render(request, "4.html")


def education(request):
    return render(request, "5.html")


def contacts(request):
    return render(request, "6.html")


def timetable(request):
    return render(request, "timetable.html")


def timetableExams(request):
    return render(request, "timetableExam.html")


def timofey(request):
    return HttpResponse("url для Тимофея")


def get_random_statistic_number():
    max_id = MainPageStatisticNumber.objects.all().aggregate(max_id=Max("id"))['max_id']
    value_list = []
    pk_list = []
    for elm in "01234":

        while True:
            pk = random.randint(1, max_id)
            if not pk in pk_list:
                break


        pk_list.append(pk)
        value = MainPageStatisticNumber.objects.filter(pk=pk).first()
        if value:
            value_list.append(value)
    return value_list


def departments(request):
    return render(request, "Departments.html")


def council(request):
    return render(request, "Council.html")



def oneWindow(request):
    return render(request, "OneWindow.html")


def mapApi(request):
    return render(request, "googleMapsApi.html")


def NwordDocuments(request):
    return render(request, "NwordDocuments.html")


def internationalConnection(request):
    return render(request, "InternationalConnection.html")


def edi(request):
    return render(request, "edi.html")