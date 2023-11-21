from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(response):
    # return HttpResponse("Pierwszy widok")
    return render(response, "articles.html")
