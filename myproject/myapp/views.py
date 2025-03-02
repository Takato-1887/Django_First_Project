from django.shortcuts import render
from .models import Feature  # Import the Feature model

def index(request):
    # Fetch all Feature objects from the database
    features = Feature.objects.all()

    # Pass the features to the template
    context = {
        "features": features,
    }

    return render(request, "index.html", context)