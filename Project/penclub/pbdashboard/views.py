from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from library.views import PenClubAccessView
from orm.models import Club,CityRegency,Anggota
from penclub.pbdashboard.forms import ClubForm
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
        form = ClubForm(request.POST or None)
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
        club = request.user.anggota.club
        data = {
            'menu' : 'club',
            'anggota':{
                'total': club.anggotas.all().count(),
                'coach_total': club.anggotas.all().filter(position='Coach').count(),
                'male_total': club.anggotas.filter(gender='Pria').count(),
                'female_total': club.anggotas.filter(gender='Wanita').count(),
            }    
        }
        return render(request, template, data)

class UbahClub(View):
    def get(self, request):
        template = 'pbdashboard/ubah_detail.html'
        data = {
            'citys': CityRegency.objects.all(),
            
        }
        return render(request, template, data)

class UpdateView(View):
    def post(self, request):
        club = request.user.anggota.club
        form = ClubForm(request.POST, request.FILES)
        if form.is_valid():
            club.user = request.user
            cityregency = CityRegency.objects.get(pk=request.POST['cityregency'])
            club.cityregency =  cityregency
            club.name = form.cleaned_data['name']
            club.register_number = form.cleaned_data['register_number']
            club.since = form.cleaned_data['since']
            club.secretariat = form.cleaned_data['secretariat']
            club.leader = form.cleaned_data['leader']
            club.slogan = form.cleaned_data['slogan']
            newlogo = form.cleaned_data.get('logo', None)
            if not newlogo == None:
                club.logo = newlogo
            club.save(force_update=True)

            return redirect('pbdashboard:detail')
        else:
            return redirect('pbdashboard:edit')