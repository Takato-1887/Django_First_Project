from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = "Priyal"
    return render(request, "index.html")

def counter(request):
    text = request.GET["text"]
    count = len(text.split())
    return render(request, "counter.html",{"count": count})