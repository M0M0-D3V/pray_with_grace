from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

# basic validator


def basic_validator(value):
    if len(value) < 3:
        raise ValidationError(
            f'{value} must be longer than 2 characters')


class Category(models.Model):
    title = models.CharField(max_length=20)
    # prayers
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    title = models.CharField(max_length=20)
    # prayers
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Prayer(models.Model):
    title = models.CharField(max_length=100, validators=[basic_validator])
    description = models.TextField()
    active = models.BooleanField(default=True)
    requested_by = models.ForeignKey(
        User, related_name="requested_prayers", on_delete=models.CASCADE)
    people_praying_for_this = models.ManyToManyField(
        User, related_name="prayers_people_are_praying_for")
    categories = models.ManyToManyField(Category, related_name="prayers")
    tags = models.ManyToManyField(Tag, related_name="prayers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# User class has relationships with Prayer:
# User.prayers.all
# User.praying_for.all
