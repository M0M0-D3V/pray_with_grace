from django.shortcuts import render
from django.contrib.auth.models import User
# from .models import User
from prayers_app.models import Prayer, Category, Tag
from users_app.models import Profile
# Create your views here.
# from django.contrib.auth import get_user_model
# User = get_user_model()
users = User.objects.all()


def profile(request):
    return render(request, "profile.html")


def members(request):

    context = {
        'all_members': users
    }
    return render(request, "members.html")
