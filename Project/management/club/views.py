from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import CityRegency, Club
from management.club.forms import ClubForm
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import LoginRequiredMixin

class HarusLogin(LoginRequiredMixin):
    login_url = 'login:view'

class ListClubView(HarusLogin,View):
    def get(self, request):

        form = ClubForm(request.POST or None)
        template = 'club/index.html'
        club = Club.objects.filter()
        cityregency = CityRegency.objects.all()
        data = {

            'form_mode' : 'add',
            'form' : form,
            'club' : club,
            'cityregency' : cityregency ,
        }
        return render(request, template, data)

class SaveClubView(HarusLogin,View):
    
    def post(self, request):
        template = 'club/index.html'

        form = ClubForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            club = Club()
            club.user = request.user
            club.cityregency = form.cleaned_data['cityregency']
            club.name = form.cleaned_data['name']
            club.register_number = form.cleaned_data['register_number']
            club.since = form.cleaned_data['since']
            club.secretariat = form.cleaned_data['secretariat']
            club.leader = form.cleaned_data['leader']
            club.slogan = form.cleaned_data['slogan']
            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   
            club.save()
            return redirect('club:view')
        else:
            club = Club.objects.all()
            data = {
                'form_mode' : 'add',
                'form': form,
                'club': club,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Disimpan !!')               
            return render(request, template, data)

class HapusClubView(HarusLogin,View):
    
    def get(self, request, id):
        club = Club.objects.filter(id=id)
        if club.exists():
            club.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('club:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')    