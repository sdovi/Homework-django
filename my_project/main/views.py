from django.shortcuts import render
from .models import airpods, iphone, watch, ipad, mac, main_card, menuwatch, akustika, aksesuar, phone, samsung, akustikamain, aksessuarmain, phonemain


def macbro(request):
    product = main_card.objects.all()
    akustika = akustikamain.objects.all()
    aksessuar = aksessuarmain.objects.all()
    phone = phonemain.objects.all()
    return render(request, "main/macbro-glavniy.html", {"product": product,
                                                        "akustika": akustika,
                                                        "aksessuar": aksessuar,
                                                        "phone": phone, })


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
    product = iphone.objects.all()
    return render(request, "main/mac_iphonemenu.html", {"product": product})


def macbrotwo(request):
    return render(request, "main/macbro_two.html", )


def macaksesuar(request):
    product = aksesuar.objects.all()
    return render(request, "main/mac_aksesuar.html", {"product": product})


def macakustika(request):
    product = akustika.objects.all()
    return render(request, "main/mac_akustika.html", {"product": product})


def macphone(request):
    product = phone.objects.all()
    return render(request, "main/mac_phone.html",  {"product": product})


def macsamsung(request):
    product = samsung.objects.all()
    return render(request, "main/mac_samsung.html", {"product": product})


def macregister(request):
    return render(request, "main/register.html")


def macall(request):
    mac1 = mac.objects.all()
    iphone1 = iphone.objects.all()
    ipad1 = ipad.objects.all()
    watch1 = watch.objects.all()
    airpods1 = airpods.objects.all()
    akustika1 = akustika.objects.all()
    aksesuar1 = aksesuar.objects.all()
    phone1 = phone.objects.all()
    samsung1 = samsung.objects.all()
    return render(request, "main/mac_all.html", {"mac": mac1,
                                                  "iphone": iphone1,
                                                  "ipad": ipad1,
                                                  "watch": watch1,
                                                  "airpods": airpods1,
                                                  "akustika": akustika1,
                                                  "aksessuar": aksesuar1,
                                                  "phone": phone1,
                                                  "samsung": samsung1, })
