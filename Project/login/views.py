from django.shortcuts import render, redirect, get_list_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from login.forms import AuthenticateForm
from django.contrib import messages
from django.conf import settings
from login.forms import AuthenticateForm


class LoginView(View):
    def get(self, request):
        template = 'login.html'
        form = AuthenticateForm(request.POST or None)
        data  = {
            'form': form
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
                if user.is_active:
                    # login
                    login(request, user) 

                    # checkbox remember 
                    if not remember:
                        settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
                        request.session.set_expiry(0)
                    else:
                        settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False

                    return redirect('member:tpl')
                else:
                    state = "Akun Anda tidak Aktiv silahkan tanya pada Administrator Web Anda."
                    messages.add_message(request, messages.ERROR, state)
            else:
                state = "Login Gagal, Username atau Password Anda Salah!."
                messages.add_message(request, messages.ERROR, state)
        data  = {
            'form': form
        }
        return render(request, template, data)
        


class DoLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login:view')