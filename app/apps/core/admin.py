from django.contrib import admin
from .models import VaccineInfo, VaccineInfoKeywords

admin.site.register(VaccineInfoKeywords)
admin.site.register(VaccineInfo)
