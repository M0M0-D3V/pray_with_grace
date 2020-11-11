from django.contrib import admin
from django.contrib.auth.models import User
from users_app.models import Profile
from prayers_app.models import Category, Tag, Prayer
# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)


class PrayerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Prayer, PrayerAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)
