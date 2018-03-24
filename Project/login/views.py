from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from login.forms import AuthenticateForm
from django.contrib import messages
from django.conf import settings
from login.forms import AuthenticateForm
from library import authcheck
from login import helpers
from orm.models import Club, CityRegency, Anggota

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

class LoginView(View):
    def get(self, request):
        template = 'login.html'
        form = AuthenticateForm(request.POST or None)
        club_anggota_labels = [club.name for club in Club.objects.all()]
        club_anggota_values = [club.anggotas.count() for club in Club.objects.all()]
        data  = {
            'form': form,
            'TotalClub' : getTotalClub(),
            'TotalAnggota' : getTotalAnggota(), 
            'club': {
                'total': Club.objects.all().count(),
                'labels': club_anggota_labels,
                'member_count': club_anggota_values,
            },
            'anggota': {
                'total': Anggota.objects.all().count(),
                'coach_total': Anggota.objects.filter(position='Coach').count()
            },
        }
        return render(request, template, data)


class DoLoginView(View):
    def post(self, request):
        template = 'login.html'
        form = AuthenticateForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember = form.cleaned_data['remember']

            # ngecek user ada apa nggak
            user = authenticate(username=username, password=password) 
            
            if user is not None:
                # checkbox remember 
                print(user.is_staff)
                
                if not remember:
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
                    request.session.set_expiry(0)
                else:
                    settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
                if authcheck.AuthCheck.isSuperUser(user):
                    login(request, user)
                    return redirect('province:view') 
                elif authcheck.AuthCheck.isPenCab(user):
                    login(request, user)
                    return redirect('pgdashboard:view') 
                elif authcheck.AuthCheck.isPenClub(user):
                    login(request, user)
                    return redirect('pbdashboard:view') 
                else:
                     messages.add_message(request, messages.WARNING,
                                 'Akun Belum Terdaftar Sebagai User !!')
            else:
                  messages.add_message(request, messages.WARNING,
                                 'Username dan atau Password tidak ditemukan !!')

        data  = {
            'form': form,
        }
        return redirect('login:view')
        return render(request, template, data)
        


class DoLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login:view')