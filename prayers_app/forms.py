from django import forms
from .models import User, Prayer, Category, Tag


class PrayerForm(forms.ModelForm):
    class Meta:
        model = Prayer
        fields = ['title', 'description']


class CreateNewPrayer(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(
        required=False, max_length=255, widget=forms.Textarea)
