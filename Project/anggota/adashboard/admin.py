from django.contrib import admin
from orm.models import Anggota

class AnggotaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Anggota, AnggotaAdmin)
