from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic import View
from login.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class LoginView(View):
    def get(self, request):
        template = 'login/dashboard.html'
        
        data = {
        }
        return render(request, template, data)