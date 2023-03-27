from django.shortcuts import render
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://sdovi:820722zz@cluster0.wan4jgq.mongodb.net/?retryWrites=true&w=majority')
db = cluster['information']
collection = db['info']

info = collection.find_one({
    "_id": 2
})

text = info

def macbro(request):
    return render(request, "main/macbro-glavniy.html",  )


def macbrotwo(request):
    return render(request, "main/macbro_two.html", )


def macmac(request):
    return render(request, "main/mac_mac.html", )


def maciphone(request):
    return render(request, "main/mac_iphone.html", )


def macipad(request):
    return render(request, "main/mac_ipad.html", )


def macwatch(request):
    return render(request, "main/mac_watch.html", )


def macair(request):
    return render(request, "main/mac_airpots.html", )


def macwatchmenu(request):
    return render(request, "main/mac_watchmenu.html", text)
