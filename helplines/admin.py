from django.contrib import admin
from .models import Allocated
# Register your models here.

@admin.register(Allocated)
class Hospitals(admin.ModelAdmin):
    list_display = ('name','hdu','oxygenated','ventilators','icu','normal','total','ahdu','aoxygenated','aventilators','aicu','anormal','atotal')