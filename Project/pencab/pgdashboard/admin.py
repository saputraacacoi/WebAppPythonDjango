from django.contrib import admin
from orm.models import PenCab

class PenCabAdmin(admin.ModelAdmin):
    pass
admin.site.register(PenCab, PenCabAdmin)
