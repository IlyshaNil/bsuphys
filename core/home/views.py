from urllib import response
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from home.models import MainPageStatisticNumber, KeyPublications, FamousGraduates
from django.utils import timezone
from django.conf import settings
from django.http import HttpResponse
from django.utils import translation
from django.db.models import Max
import random
from django.shortcuts import redirect
import pprint
from django.http import HttpResponse
import os
import hashlib
import hmac
import hmac
from hashlib import sha1
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import hashlib
import hmac
import json
from dynaconf import settings as _settings

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

import requests
from ipaddress import ip_address, ip_network


from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import force_bytes


def language_switch_en(request):
    user_language = "en"
    translation.activate(user_language)
    response = HttpResponse(status=302)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)

    refresh_path = request.path[: request.path.find("/language_en")]

    refresh_path = refresh_path.replace("/ru/", "/en/")
    response["Location"] = refresh_path
    return response


def language_switch_ru(request):
    user_language = "ru"
    translation.activate(user_language)
    response = HttpResponse(status=302)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)

    refresh_path = request.path[: request.path.find("/language_ru")]
    refresh_path = refresh_path.replace("/en/", "/ru/")
    response["Location"] = refresh_path
    return response


def language_switch_en_main(request):
    user_language = "en"
    translation.activate(user_language)
    response = HttpResponse(status=302)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    response["Location"] = "/"
    return response


def language_switch_ru_main(request):
    user_language = "ru"
    translation.activate(user_language)
    response = HttpResponse(status=302)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    response["Location"] = "/"
    return response


def index(request):
    post = Post.published.latest("publish")
    lastKeyPub = KeyPublications.objects.order_by("-id")[:3]
    # if MainPageStatisticNumber.objects.count() > 3 and FamousGraduates.objects.count() > 2:
    randomNumbers = get_random_statistic_number(MainPageStatisticNumber, 4)
    random_alumnu = get_random_statistic_number(FamousGraduates, 3)
    return render(
        request,
        "main.html",
        {
            "post": post,
            "stat1": randomNumbers[0],
            "stat2": randomNumbers[1],
            "stat3": randomNumbers[2],
            "stat4": randomNumbers[3],
            "pub1": lastKeyPub[0],
            "pub2": lastKeyPub[1],
            "pub3": lastKeyPub[2],
            "graduates": random_alumnu,
        },
    )
    # else:
    #     return HttpResponse("200 OK")


def alum_detail(request, alum):
    alum = get_object_or_404(FamousGraduates, slug=alum,)
    return render(request, "alumPersonTemplate.html", {"alum": alum})


def alums_list(request):
    object_list = FamousGraduates.objects.all().order_by("shortDescription")
    return render(request, "listPersonTemplate.html", {"alums": object_list},)


def templates(request):
    posts = Post.published.latest("publish")
    return render(request, "template1.html", {"posts": posts})


def keyPublications(request):
    publications = reversed(KeyPublications.objects.all())
    return render(request, "publicationsTemplate.html", {"works": publications},)


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


def timetableMag(request):
    return render(request, "timetablemag.html")


def timetableExams(request):
    return render(request, "timetableExam.html")


def timofey(request):
    return HttpResponse("url для Тимофея")


def get_random_statistic_number(model_class, amount):
    max_id = list(model_class.objects.values('id'))
    value_list = []
    pk_list = []
    for elm in range(0, amount):
        while True:
            pk = random.randint(0, len(max_id)-1)
            if not pk in pk_list:
                break

        pk_list.append(pk)
        value = model_class.objects.get(pk=max_id[pk]['id'])
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
    return render(request, "worldwide.html")


def edi(request):
    return render(request, "edi.html")


def ckpMain(request):
    return render(request, "CKP/index.html")


def linesOfResearches(request):
    return render(request, "CKP/lines-of-researches.html")


def measurementProcedures(request):
    return render(request, "CKP/measurement-procedures.html")


def equipment(request):
    return render(request, "CKP/equipment.html")


def contactsCKP(request):
    return render(request, "CKP/contacts.html")


def scientificServices(request):
    return render(request, "CKP/scientific-services.html")


def conferences(request):
    return render(request, "conferences.html")


def nilAndScienceDirections(request):
    return render(request, "nilAndScienceDir.html")


def eduProcess(request):
    return render(request, "eduProcess.html")


def test(request):
    return render(request, "worldwide.html")


def dod(request):
    return render(request, "dod.html")


def secondStage(request):
    return render(request, "secondStage.html")


def keyPublicationsListAll(request):
    return render(request, "PublicationsAll.html")


def servicePage(request):
    return render(request, "servicePage.html")


def studOlimp2021(request):
    return render(request, "studOlimp2021.html")


def abiturOlimp2021(request):
    return render(request, "abiturOlimp.html")


def raspred(request):
    return render(request, "raspred.html")


def wellcome(request):
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


def tutor(request):
    return render(request, "tutorService.html")


def educations(request):
    return render(request, "EducationalWork.html")


def services(request):
    return render(request, "theFacultyServices.html")


def worldbank(request):
    return render(request, "theWorldBankProj.html")


def build_squad(request):
    return render(request, "build-suqad.html")


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def aboba(request):
    meta = request.META.items()
    return HttpResponse(meta)


def tradeUnion(request):
    return render(request, "primaryTradeUnionCommitee.html")


def development(request):
    return render(request, "theFacultyEquipmAndSoftware.html")


def scienceSchool(request):
    return render(request, "ScienceSchools.html")


def youthOrganizations(request):
    return render(request, "YouthOrganizations.html")


def prRules(request):
    return render(request, "rulesOfConductOfTeachingEmployees.html")


def PublicationsInArchive(request):
    return render(request, "PublicationsInArchive.html")


def thirdStage(request):
    return render(request, "thirdStage.html")


def updateGithub(request):
    if ifGithubHook(request) and verifyGithubToken(request):
        os.system('sudo bash /home/dev/cicd')
    return HttpResponse("Hello")

@require_POST
@csrf_exempt
def ifGithubHook(request):
    # Verify if request came from GitHub
    forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))
    client_ip_address = ip_address(forwarded_for)
    whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            break
    else:
        return HttpResponseForbidden('Permission denied.')

    return HttpResponse('pong')


def verifyGithubToken(request):
    # Verify if request came from GitHub
    # ...

    # Verify the request signature
    header_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
    if header_signature is None:
        return HttpResponseForbidden('Permission denied.')

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        return HttpResponseServerError('Operation not supported.', status=501)

    mac = hmac.new(force_bytes(_settings.GITHUB_WEBHOOK_KEY), msg=force_bytes(request.body), digestmod=sha1)
    if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
        return HttpResponseForbidden('Permission denied.')

    # If request reached this point we are in a good shape
    return HttpResponse('pong')


@require_POST
@csrf_exempt
def handle_github_hook(request):
    # Verify if request came from GitHub
    forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))
    client_ip_address = ip_address(forwarded_for)
    whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            break
    else:
        return HttpResponseForbidden('Permission denied.')

    # Verify the request signature
    header_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
    if header_signature is None:
        return HttpResponseForbidden('Permission denied.')

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        return HttpResponseServerError('Operation not supported.', status=501)

    mac = hmac.new(force_bytes(settings.GITHUB_WEBHOOK_KEY), msg=force_bytes(request.body), digestmod=sha1)
    if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
        return HttpResponseForbidden('Permission denied.')

    # If request reached this point we are in a good shape
    # Process the GitHub events
    event = request.META.get('HTTP_X_GITHUB_EVENT', 'ping')

    if event == 'ping':
        return HttpResponse('pong')
    elif event == 'push':
        # Deploy some code for example
        return HttpResponse('success')

    # In case we receive an event that's not ping or push
    return HttpResponse(status=204)
    # # Check the X-Hub-Signature header to make sure this is a valid request.
    # if 'X-Hub-Signature-256' in request.headers:
    #     github_signature = request.headers['X-Hub-Signature-256']
    # else:
    #     return HttpResponseForbidden("x-hub-signature-256 header is missing!")
    # hash_object = hmac.new(_settings.GITHUB_WEBHOOK_KEY.encode('utf-8'), msg=request.body, digestmod=hashlib.sha256)
    # expected_signature = "sha256=" + hash_object.hexdigest()
    # if not hmac.compare_digest(expected_signature, github_signature):
    #     return HttpResponseForbidden("x-hub-signature-256 header isn't match!")
    
    # return HttpResponse("200")
    
    