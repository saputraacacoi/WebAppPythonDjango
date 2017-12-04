from django.contrib import admin
from orm.models import Province

class ProvinceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Province, ProvinceAdmin)
