from django.contrib import admin
from .models import Image

class imageAdmin(admin.ModelAdmin):
    list_display = ["title", "image_tag", "photo"] # new

admin.site.register(Image, imageAdmin)