from django.contrib import admin
from orm.models import Member

class MemberAdmin(admin.ModelAdmin):
    pass
admin.site.register(Member, MemberAdmin)
