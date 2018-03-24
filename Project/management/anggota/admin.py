from django.contrib import admin
from orm.models import Anggota

@admin.register(Anggota)
class AnggotaAdmin(admin.ModelAdmin):
    pass

