from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import CityRegency, Province
from django.contrib.auth.mixins import LoginRequiredMixin
from management.cityregency.forms import CityRegencyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from library.views import ManagementAccessView


class ListCityRegencyView(ManagementAccessView):
    def get(self, request):

        form = CityRegencyForm(request.POST or None)
        template = 'cityregency/index.html'
        province = Province.objects.all()
        cityregency = CityRegency.objects.filter()
        data = {

            'form_mode' : 'add',
            'form' : form,
            'province' : province,
            'cityregency' : cityregency ,
        }
        return render(request, template, data)

class SaveCityRegencyView(ManagementAccessView):
    
    def post(self, request):
        template = 'cityregency/index.html'
        form = CityRegencyForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            cityregency = CityRegency()
            cityregency.user = request.user
            cityregency.name = form.cleaned_data['name']
            cityregency.province = form.cleaned_data['province']
            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   
            cityregency.save()
            return redirect('cityregency:view')
        else:
            cityregency = CityRegency.objects.all()
            data = {
                'form_mode' : 'add',
                'form': form,
                'cityregency': cityregency,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Disimpan !!')               
            return render(request, template, data)

class EditCityRegencyView(ManagementAccessView):
    template = 'cityregency/index.html'

    def get(self, request, id):
        cityregency = CityRegency.objects.filter(id=id)
        if not cityregency.exists():
            return redirect('cityregency:view')
        cityregency = cityregency.first()
        initial = {

            'id': cityregency.id,
            'name': cityregency.name,
            'province': cityregency.province,
        }

        form = CityRegencyForm(initial=initial)
        cityregency = CityRegency.objects.all()
        data = {
            'id':id,
            'form': form,
            'form_mode' : 'edit',
            'cityregency' : cityregency,
        }
        return render(request, self.template, data)


class UpdateCityRegencyView(ManagementAccessView):

    def post(self, request):
        
        template = "cityregency/index.html"
        form = CityRegencyForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            cityregency = CityRegency.objects.get(pk=id)
            cityregency.name = form.cleaned_data['name']
            cityregency.province = form.cleaned_data['province']
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')               
            cityregency.save(force_update=True)
            return redirect('cityregency:view')
        else:
            cityregency = CityRegency.objects.all()
            data    =  {
                'form_mode':'edit',
                'form': form,
                'cityregency': cityregency,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Diupdate !!')                           
            return render(request, template, data)

class HapusCityRegencyView(ManagementAccessView):

    def get(self, request, id):
        cityregency = CityRegency.objects.filter(id=id)
        if cityregency.exists():
            cityregency.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('cityregency:view')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')          