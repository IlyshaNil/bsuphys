from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Advertisement, QuantumCourse


# Create your views here.

def quantumMain(request):
    return render(request, "quantumSchoolMain.html")

def quantumUni(request):
    return render(request, "quantumSchoolUni.html")

def quantumNine(request):
    return render(request, "quantumSchool9.html")

def quantumTen(request):
    return render(request, "quantumSchool10.html")

def quantumEleven(request):
    return render(request, "quantumSchool11.html")

def quantumOlimp(request):
    return render(request, "quantumSchoolOlimp.html")

def quantumAdvertisement(request):
    quantCourse = request.path.split("/")[3]

    if quantCourse == "quantum-olimp":
        object = QuantumCourse.objects.get(course = "1")
        courseAds = object.advertisement.all()
        return render(request, "quantumSchoolAds.html", {"courseAds": courseAds})

    if quantCourse == "quantum-11":
        object = QuantumCourse.objects.get(course = "2")

    if quantCourse == "quantum-10":
        object = QuantumCourse.objects.get(course = "3")

    if quantCourse == "quantum-9":
        object = QuantumCourse.objects.get(course = "4")

    if quantCourse == "quantum-uni":
        object = QuantumCourse.objects.get(course = "5")

    return HttpResponse(html)