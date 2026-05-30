from django.shortcuts import render, redirect

from .forms import TravelForm
from .models import *
# Create your views here.
def index(request):
    destinations = Travel.objects.all()
    return render(request, "index.html", {"destinations": destinations})

def add_destination(request):
    if request.method == "POST":
        form = TravelForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save(commit=False)
            tour.tour_guide = request.user.tourguide
            tour.full_clean()  # Повикај clean() повторно со tour_guide
            tour.save()
            return redirect('index')
    form = TravelForm()
    return render(request, 'add_destination.html', {"form": form})