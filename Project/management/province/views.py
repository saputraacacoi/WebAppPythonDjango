from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib import messages
from orm.models import Province
from management.province.forms import ProvinceForm
from django.contrib.auth.mixins import LoginRequiredMixin   
from library.views import ManagementAccessView
from management.province import helpers
from orm.models import TestGrafik

def getLineChart():
    dataTitle = 'Penjualan'
    dt = [20,15,23,14,23,22,30,20,15,30,35,40]
    lb = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul','Agust','Sept','Okto','Nov','Des']      
    lc = helpers.lineChartHelper(dataTitle, dt, lb)
    return lc

def getTestGrafikLine():
    all_test_grafik = TestGrafik.objects.all()
    pbusur = all_test_grafik.filter(k_busur='Ya').count()
    tpbusur = all_test_grafik.filter(k_busur='Tidak').count()
    dataTitle = 'Total Penjualan PerItem'
    dt = [pbusur,tpbusur]
    lb = ['Sembako', 'Snack']  
    lc = helpers.TestGrafikLine(dataTitle, dt, lb)
    return lc

def getTestGrafikGender():
        all_test_gender = TestGrafik.objects.all()
        pria = all_test_gender.filter(gender='Pria').count()
        wanita = all_test_gender.filter(gender='Wanita').count()
        dataTitle = 'Jenis Kelamin'
        dt = [pria,wanita]
        lb = ['Pria', 'Wanita']  
        lc = helpers.TestGrafikGender(dataTitle, dt, lb)
        return lc
    
class ListProvinceView(ManagementAccessView):
    def get(self, request):  
        form = ProvinceForm(request.POST or None)
        template = 'province/index.html'
        province = Province.objects.all()
        data = {
            'form_mode': 'add',
            'province' : province,
            'form' : form,
            'lineChart' : getLineChart(),
            'TestGrafikLine' : getTestGrafikLine(),
            'TestGrafikGender' : getTestGrafikGender(),
        }
        return render(request, template, data)

class SaveProvinceView(ManagementAccessView):
    def post(self, request):
        
        template = 'province/index.html'
        form = ProvinceForm(request.POST or None)
        if form.is_valid():
            # dari ngambil data
            # sampai simpan data
            province = Province()
            province.user = request.user
            province.name = form.cleaned_data['name']
            province.save()
            messages.add_message(request, messages.INFO, 'Data Berhasil Disimpan')   
            return redirect('province:view')
        else:
            province = Province.objects.all()
            data = {
                'form_mode':'add',
                'form': form,
                'province': province,
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Disimpan !!')               
            return render(request, template, data)

class EditProvinceView(ManagementAccessView):
    template = 'province/index.html'
    def get(self, request, id):
        
        province = Province.objects.filter(id=id)
        if not province.exists():
            return redirect('province:view')

        province = province.first()

        initial = {

            'id': province.id,
            'name': province.name,
        }

        form = ProvinceForm(initial=initial)
        province = Province.objects.all()        
        data = {

            'id': id,
            'form_mode':'edit',
            'province': province,
            'form': form,
        }
        return render(request, self.template, data)

class UpdateProvinceView(ManagementAccessView):
    def post(self, request):
        
        template = "province/index.html"
        form = ProvinceForm(request.POST or None)
        if form.is_valid():
            id = form.cleaned_data['id']
            province = Province.objects.get(pk=id)
            province.name = form.cleaned_data['name']
            province.save(force_update=True)
            messages.add_message(request, messages.INFO, 'Data Berhasil Diupdate')               
            return redirect('/province/')
        else:
            province = Province.objects.all()
            data =  {
                'form_mode':'edit',
                'form': form,
                'province': province
            }
            messages.add_message(request, messages.INFO, 'Data Gagal Diupdate !!')                           
            return render(request, template, data)


class HapusProvinceView(ManagementAccessView):

    def get(self, request, id):
        province = Province.objects.filter(id=id)
        if province.exists():
            province.first().delete()
            messages.add_message(request, messages.INFO, 'Data Berhasil Dihapus')                                       
            return redirect('/province/')
        else:
            messages.add_message(request, messages.INFO, 'Data Gagal Dihapus !!')                                       
                    