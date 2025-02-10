from django.shortcuts import render
from .models import Circle

def index(request):
    # Define the radius (no user input in this example)
    radius = 5.0

    # Create a Circle instance
    circle = Circle(radius=radius)

    # Calculate area and circumference
    area = circle.area()
    circumference = circle.circumference()

    # Pass the results to the template
    context = {
        "radius": radius,
        "area": area,
        "circumference": circumference,
    }

    return render(request, "index.html", context)
def counter(request):
    text = request.POST["text"]
    count = len(text.split())
    return render(request, "counter.html",{"count": count})