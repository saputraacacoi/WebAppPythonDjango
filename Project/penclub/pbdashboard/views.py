from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from library.views import PenClubAccessView
from orm.models import Club,CityRegency,Anggota
from penclub.pbdashboard.forms import PenClubForm
from penclub.pbdashboard import helpers

def getTotalClub():
    label = []
    data = []
    crall = CityRegency.objects.all()
    for cr in crall:
        label.append(cr.name)
        c = len(Club.objects.filter(cityregency__name=cr.name))
        data.append(c)
    lc = helpers.HelpersPenclub(label, data)
    return lc

def getTotalAnggota():
    label = []
    data = []
    cball = Club.objects.all()
    for cr in cball:
        label.append(cr.name)
        c = len(Anggota.objects.filter(club__name=cr.name))
        data.append(c)
    lc = helpers.HelpersPenclub(label, data)
    return lc

class ListPenClubView(PenClubAccessView):
    def get(self, request):
        form = PenClubForm(request.POST or None)
        template = 'pbdashboard/index.html'
        data = {
            'form_mode': 'add',
            'form' : form,
            'TotalClub' : getTotalClub(),
            'TotalAnggota' : getTotalAnggota(),
        }
        return render(request, template, data)

class DetailClub(View):
    def get(self, request):
        template = 'pbdashboard/detail.html'
        data = {
        }
        return render(request, template, data)