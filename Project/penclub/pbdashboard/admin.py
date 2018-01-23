from django.contrib import admin
from orm.models import PenClub

class PenClubAdmin(admin.ModelAdmin):
    pass
admin.site.register(PenClub, PenClubAdmin)

