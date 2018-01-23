from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from library.views import PenCabAccessView
from orm.models import PenCab
from pencab.pgdashboard.forms import PenCabForm

class ListPencabView(PenCabAccessView):
    def get(self, request):
        
        form = PenCabForm(request.POST or None)
        template = 'pgdashboard/index.html'
        pencab = PenCab.objects.all()
        data = {
            'form_mode': 'add',
            'pencab' : pencab,
            'form' : form,
        }
        return render(request, template, data)
