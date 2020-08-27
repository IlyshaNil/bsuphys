from django.shortcuts import render


# Create your views here.

def quantumMain(request):
    return render(request, "quantumSchoolMain.html")

def quantumUni(request):
    return render(request, "quantumSchoolUni.html")

def quantumNine(request):
    return render(request)

def quantumTen(request):
    return render(request)

def quantumEleven(request):
    return render(request)

def quantumOlimp(request):
    return render(request, "quantumSchoolOlimp.html")

