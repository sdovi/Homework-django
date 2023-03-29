from django.shortcuts import render
from .models import airpods, iphone, watch, ipad, mac, main_card, menuwatch,iphonemenu


def macbro(request):
    product = main_card.objects.all()
    return render(request, "main/macbro-glavniy.html", {"product": product})


def macmac(request):
    product = mac.objects.all()
    return render(request, "main/mac_mac.html", {"product": product})


def maciphone(request):
    product = iphone.objects.all()
    return render(request, "main/mac_iphone.html", {"product": product})


def macipad(request):
    product = ipad.objects.all()
    return render(request, "main/mac_ipad.html", {"product": product})


def macwatch(request):
    product = watch.objects.all()
    return render(request, "main/mac_watch.html", {"product": product})


def macair(request):
    product = airpods.objects.all()
    return render(request, "main/mac_airpots.html", {"product": product})


def macwatchmenu(request):
    product = menuwatch.objects.all()
    return render(request, "main/mac_watchmenu.html", {"product": product})

def maciphonemenu(request):
    product = iphonemenu.objects.all()
    return render(request, "main/mac_iphonemenu.html", {"product": product})



def macbrotwo(request):
    return render(request, "main/macbro_two.html", )
