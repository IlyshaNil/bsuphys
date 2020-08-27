from django.shortcuts import render


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

