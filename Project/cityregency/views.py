from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import CityRegency
from django.contrib.auth.mixins import LoginRequiredMixin
from cityregency.forms import CityRegencyForm
from django.contrib.auth.mixins import LoginRequiredMixin

class HarusLogin(LoginRequiredMixin):
    login_url = 'login:view'

class ListCityRegencyView(HarusLogin,View):
    def get(self, request):
        template = 'cityregency/index.html'
        cityregency = CityRegency.objects.all()
        data = {
            'cityregency' : cityregency ,
        }
        return render(request, template, data)
class AddCityRegencyView(HarusLogin,View):
    def get(self, request):
        template = 'cityregency/add_cityregency.html'

        form = CityRegencyForm(request.POST or None)
        data = {
            'form': form,
        }

        return render(request, template, data)

class SaveCityRegencyView(HarusLogin,View):
    
    def post(self, request):
        template = 'cityregency/add_cityregency.html'

        form = CityRegencyForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            cityregency = CityRegency()
            cityregency.user = request.user
            cityregency.name = form.cleaned_data['name']
            cityregency.save()
            
            return redirect('cityregency:view')
        else:
            
            data = {
                'form': form,
            }

            return render(request, template, data)

class EditCityRegencyView(HarusLogin,View):
    template = 'cityregency/edit_cityregency.html'

    def get(self, request, id):
        cityregency = CityRegency.objects.get(pk=id)
        initial = {
            'id': cityregency.pk,
            'name': cityregency.name,
        }

        form = CityRegencyForm(initial=initial)
        data = {
            'form': form
        }
        return render(request, self.template, data)


class UpdateCityRegencyView(HarusLogin,View):

    def post(self, request):

        form = CityRegencyForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            cityregency = CityRegency.objects.get(pk=id)
            cityregency.name = form.cleaned_data['name']
            cityregency.save(force_update=True)
            return redirect('/cityregency/')


class HapusCityRegencyView(HarusLogin,View):

    def get(self, request, id):
        cityregency = CityRegency.objects.get(pk=id)
        if cityregency:
            cityregency.delete()
            return redirect('/cityregency/')        