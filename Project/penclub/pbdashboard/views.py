from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from library.views import PenClubAccessView
from orm.models import Club, CityRegency, Anggota,  ClubFiles, PenClub
from penclub.pbdashboard.forms import ClubForm, BerkasForm, UserForm, MemberForm 
import mimetypes
import os

class DetailClubView(PenClubAccessView):
    def get(self, request):
        template = 'pbdashboard/detail_club.html'
        form = ClubForm(request.POST or None)
        club = request.user.anggota.club
        data = {
            'menu' : 'club',
            'form' : form,
            'anggota':{
                'total': club.anggotas.all().count(),
                'coach_total': club.anggotas.all().filter(position='Coach').count(),
                'male_total': club.anggotas.filter(gender='Pria').count(),
                'female_total': club.anggotas.filter(gender='Wanita').count(),
            }    
        }
        return render(request, template, data)

class UbahClubView(PenClubAccessView):
    def get(self, request):
        template = 'pbdashboard/ubah_club.html'
        data = {
            'citys': CityRegency.objects.all(),
            
        }
        return render(request, template, data)

class UpdateClubView(PenClubAccessView):
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

class BerkasView(PenClubAccessView):
    def get(self, request):
        template = 'pbdashboard/berkas.html'
        form = BerkasForm(request.POST, request.FILES)
        data = {
            'form': form
        }
        return render(request, template, data)

class BerkasUploadView(PenClubAccessView):
    def post(self, request):
        form = BerkasForm(request.POST or None, request.FILES)
        if form.is_valid():
            club_file = ClubFiles()
            club_file.club = request.user.anggota.club
            club_file.file = form.cleaned_data['file']
            club_file.mimetype = mimetypes.guess_type(
                club_file.file.name)[0].split('/')[0]
            club_file.file_ext = mimetypes.guess_type(
                club_file.file.name)[0].split('/')[1]
            club_file.filename = club_file.file.name

            club_file.save()

            return HttpResponse('Success')
        return redirect('pbdashboard:documents')

class HapusBerkasView(PenClubAccessView):
    
    def get(self, request, pk):
        obj = ClubFiles.objects.get(pk=pk)
        if obj:
            img_url = os.path.join(os.getcwd(), obj.file.url[1:])
            obj.delete()
            if os.path.exists(img_url):
                os.remove(img_url)
                
            return redirect('pbdashboard:documents')

class ListAnggotaView(PenClubAccessView):
    def get(self, request):
        anggota = Anggota.objects.filter(club=self.request.user.anggota.club)
        form = ClubForm(request.POST or None)
        template = 'pbdashboard/view_anggota.html'
        data = {
            'anggota' : anggota,
            'form' : form,
        }
        return render(request, template, data)

class DetailAnggotaView(PenClubAccessView):
    def get(self, request, pk):
        template = 'pbdashboard/detail_anggota.html'
        data = {
            'anggota' : Anggota.objects.get(club=request.user.anggota.club, pk=pk)
        }
        return render(request, template, data)

class AddAnggotaView(PenClubAccessView):
    def get(self, request):
        template = 'pbdashboard/add_anggota.html'
        user_form = UserForm(request.POST or None)
        anggota_form = MemberForm(request.POST or None)
       
        data = {
            'user_form' : user_form,
            'member_form' : anggota_form,

        }
        return render(request, template, data)

class SaveAnggotaView(PenClubAccessView):
    def post(self, request):
        anggota_form = MemberForm(request.POST or None)

        if anggota_form.is_valid():
            user = User()
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            staff = request.POST.get('staff', None)
            if not staff == None:
                user.is_staff = True
                user.save()

                group = Group.objects.get(name='Penclub')
                group.user_set.add(user)

                penclub = PenClub()
                penclub.user = user
                penclub.name = user.username
                penclub.save()

            else:
                 user.save()

            anggota = Anggota()
            anggota.user = user
            anggota.club = request.user.anggota.club
            anggota.name = anggota_form.cleaned_data['nama']
            anggota.adress = anggota_form.cleaned_data['alamat']
            anggota.gender = anggota_form.cleaned_data['gender']
            anggota.born_date = anggota_form.cleaned_data['tanggal_lahir']
            anggota.phone = anggota_form.cleaned_data['no_hp']
            anggota.draw_length = anggota_form.cleaned_data['panjang_tarikan']
            anggota.position = anggota_form.cleaned_data['posisi']
            newpic = anggota_form.cleaned_data.get('picture', None)
            if not newpic == None:
                user.profile = newpic
            anggota.save()
            return redirect('pbdashboard:anggota')
        else:
            return HttpResponse(anggota_form.errors)

class HapusAnggotaView(PenClubAccessView):
    
    def get(self, request, id):
        anggota = Anggota.objects.filter(id=id)
        if anggota.exists():
            anggota.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('pbdashboard:anggota')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!') 