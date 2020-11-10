from django import forms
from .models import User, Prayer, Category, Tag


class PrayerForm(forms.ModelForm):
    class Meta:
        model = Prayer
        fields = ['title', 'description']
