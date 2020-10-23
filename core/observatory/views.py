from django.shortcuts import render

def observatoryMain(request):
    return render(request, "observatoryMain.html")


def observatoryEmployee(request):
    return render(request, "observatoryEmployee.html")


def observatoryEquipment(request):
    return render(request, "observatoryEquipment.html")


def observatoryContacts(request):
    return render(request, "observatoryContacts.html")


def observatoryPopular(request):
    return render(request, "observatoryPopular.html")