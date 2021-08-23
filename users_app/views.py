from django.shortcuts import render
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# from .models import User
from prayers_app.models import Prayer, Category, Tag
from users_app.models import Profile
# Create your views here.


def profile(request):
    return render(request, "profile.html")


def members(request):
    User = get_user_model()
    users = User.objects.all()
    context = {
        'all_members': users
    }
    return render(request, "members.html", context)

def login(request):
    pass

def register(request):
    pass
def logout(request):
    pass