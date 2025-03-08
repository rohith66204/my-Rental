from django.contrib import admin
from .models import sell,sigin
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class sellAdmin(admin.ModelAdmin):
    list_display=['housename','house_type','price','location','image','description']
admin.site.register(sell,sellAdmin)


admin.site.register(sigin, UserAdmin)


# admin
