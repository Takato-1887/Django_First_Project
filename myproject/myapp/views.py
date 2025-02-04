from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.
def index(request):
    name = "Priyal"
    feature1 = Feature()
    feature1.id = 0
    feature1.name = "Hello Guys"
    feature1.details="This is my django project"


    return render(request, "index.html", {"feature": feature1})

def counter(request):
    text = request.POST["text"]
    count = len(text.split())
    return render(request, "counter.html",{"count": count})