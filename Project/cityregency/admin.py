from django.contrib import admin
from orm.models import CityRegency

class CityRegencyAdmin(admin.ModelAdmin):
    pass
admin.site.register(CityRegency, CityRegencyAdmin)
