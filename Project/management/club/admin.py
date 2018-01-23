from django.contrib import admin
from orm.models import Club

class ClubAdmin(admin.ModelAdmin):
    pass
admin.site.register(Club, ClubAdmin)
