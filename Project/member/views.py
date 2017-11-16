from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse

class TestView(View):
    def get(self, request):
        return HttpResponse('<h1>Coba Testing tanpa menggunakan Template</h1>')

class Tsttemplate(View):
    def get(Self, request):
        template = 'member/index.html'
        data = {
            'text' : 'this is fuc',
            'ar' : [1,2,3,4],
            'logika' : True
        }
        return render(request, template, data)
