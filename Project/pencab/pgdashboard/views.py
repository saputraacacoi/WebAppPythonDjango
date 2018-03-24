from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from library.views import PenCabAccessView
from orm.models import PenCab,CityRegency,Province, Club
from pencab.pgdashboard.forms import PenCabForm
from pencab.pgdashboard import helpers

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

class ListPencabView(PenCabAccessView):
    def get(self, request):
        
        form = PenCabForm(request.POST or None)
        template = 'pgdashboard/detail_cabang.html'
        pencab = request.user.cityregency.province
        data = {
            'TotalClub' : getTotalClub(),
            'menu' : 'club',
            'form' : form,
        }
        return render(request, template, data)
