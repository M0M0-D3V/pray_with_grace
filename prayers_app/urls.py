from django.urls import path
from . import views

app_name = 'prayers'
urlpatterns = [
    path('new', views.new_prayer, name='new_prayer'),
]
