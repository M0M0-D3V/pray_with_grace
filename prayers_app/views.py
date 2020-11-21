from django.shortcuts import render, redirect
from .forms import PrayerForm, CreateNewPrayer
from prayers_app.models import Prayer, Category, Tag

# Create your views here.


def new_prayer(request):
    form = CreateNewPrayer()
    context = {
        "prayerForm": form,
        'all_my_prayers': Prayer.objects.filter(requested_by=request.user)
    }
    return render(request, "new_prayer.html", context)


def create(request):
    if request.method == 'POST':
        print(f'POST is {request.POST}')
        bound_form = PrayerForm(request.POST)
        if bound_form.is_valid():
            this_prayer = Prayer.objects.create(
                title=request.POST['title'], description=request.POST['description'], requested_by=request.user)
            print(f'prayer was created {this_prayer.title}')
            return redirect('prayers:new_prayer')
        else:
            print(bound_form.errors)
            return redirect('prayers:new_prayer')
