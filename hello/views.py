from django.shortcuts import render, redirect

from hello.models import *

import os

# Create your views here.


def home(request):
    contex = {"page": "Home"}
    return render(request, "home.html", contex)


def info(request):
    contex = {"page": "Info"}

    if request.method == "POST":
        data = request.POST
        name = data.get("FullName")
        dec = data.get("Description")
        img = request.FILES.get("Image")

        Students.objects.create(name=name, dec=dec, img=img)
        return redirect("info")

    return render(request, "info.html", contex)


def display(request):
    query_set = Students.objects.all()
    contex = {"page": "Display", "data": query_set}
    return render(request, "display.html", contex)


def delete(request, id):
    query_set = Students.objects.get(id=id)         # query_set = Students.objects.filter(id=id)
    os.remove(query_set.img.path)                   # os.remove(query_set[0].img.path) # because filter gives list of objects
    query_set.delete()
    return redirect("display")


def update(request, id):
    query_set = Students.objects.get(id=id)
    old_path = query_set.img.path
    if request.method == "POST":
        data = request.POST
        name = data.get("FullName")
        dec = data.get("Description")
        img = request.FILES.get("Image")

        query_set.name = name
        query_set.dec = dec

        if img:
            os.remove(old_path)
            query_set.img = img

        query_set.save()
        return redirect("display")

    return render(
        request, "update.html", context={"student": query_set, "page": "Update"}
    )
