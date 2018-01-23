from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from braces import views


class ManagementAccessView(views.LoginRequiredMixin, views.SuperuserRequiredMixin, views.GroupRequiredMixin, generic.View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    group_required = u"Administrator"

class PenCabAccessView(views.LoginRequiredMixin, views.StaffuserRequiredMixin, views.GroupRequiredMixin ,generic.View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    group_required = u"Pencab"

class PenClubAccessView(views.LoginRequiredMixin, views.StaffuserRequiredMixin, views.GroupRequiredMixin, generic.View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    group_required = u"Penclub"

class AnggotaAccessView(views.LoginRequiredMixin, views.GroupRequiredMixin, generic.View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    group_required = u"Anggota"