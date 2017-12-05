from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Province
from province.forms import ProvinceForm
from django.contrib.auth.mixins import LoginRequiredMixin

class HarusLogin(LoginRequiredMixin):
    login_url = 'login:view'

class ListProvinceView(HarusLogin,View):
    def get(self, request):
        template = 'province/index.html'
        province = Province.objects.all()
        data = {
            'province' : province,
        }
        return render(request, template, data)

class AddProvinceView(HarusLogin,View):
    def get(self, request):
        template = 'province/add_province.html'

        form = ProvinceForm(request.POST or None)
        data = {
            'form': form,
        }

        return render(request, template, data)

class SaveProvinceView(HarusLogin,View):
    
    def post(self, request):
        template = 'province/add_province.html'

        form = ProvinceForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            province = Province()
            province.user = request.user
            province.name = form.cleaned_data['name']
            province.save()
            
            return redirect('province:view')
        else:
            
            data = {
                'form': form,
            }

            return render(request, template, data)

class EditProvinceView(HarusLogin,View):
    template = 'province/edit_province.html'

    def get(self, request, id):
        province = Province.objects.get(pk=id)
        initial = {
            'id': province.pk,
            'name': province.name,
        }

        form = ProvinceForm(initial=initial)
        data = {
            'form': form
        }
        return render(request, self.template, data)


class UpdateProvinceView(HarusLogin,View):

    def post(self, request):

        form = ProvinceForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            province = Province.objects.get(pk=id)
            province.name = form.cleaned_data['name']
            province.save(force_update=True)
            return redirect('/province/')


class HapusProvinceView(HarusLogin,View):

    def get(self, request, id):
        province = Province.objects.get(pk=id)
        if province:
            province.delete()
            return redirect('/province/')        