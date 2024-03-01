from django.contrib import admin
from .models import *

# Register your models here.
class Signin_dispay(admin.ModelAdmin):
    list_display=['username','password']

admin.site.register(Signin)
