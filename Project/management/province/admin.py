from django.contrib import admin
from orm.models import Province
from orm.models import TestGrafik

class ProvinceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Province, ProvinceAdmin)

class TestGrafikAdmin(admin.ModelAdmin):
    pass
admin.site.register(TestGrafik, TestGrafikAdmin)