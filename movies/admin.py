from django.contrib import admin

from movies.models import Image, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
