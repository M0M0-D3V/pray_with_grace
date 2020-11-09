from django.shortcuts import render, redirect
from .forms import PrayerForm

# Create your views here.


def new_prayer(request):
    form = PrayerForm()
    context = {
        "prayerForm": form
    }
    return render(request, "new_prayer.html", context)


def create(request):
    pass
