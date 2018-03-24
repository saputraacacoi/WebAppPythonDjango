from django import forms
from orm.models import CityRegency, Club, ClubFiles, Anggota
from django.contrib.auth.models import User



class ClubForm(forms.Form):
    name = forms.CharField(max_length=100)
    register_number = forms.CharField(max_length=100)
    since = forms.CharField(max_length=100)
    secretariat = forms.CharField()
    leader = forms.CharField(max_length=100)
    slogan = forms.CharField()
    logo = forms.ImageField(required=False)

    class Meta:
        model = Club

class BerkasForm(forms.Form):
    file = forms.FileField()

    class Meta:
        model = ClubFiles

class UserForm(forms.Form):
    user = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User

class MemberForm(forms.Form):
    nama = forms.CharField(max_length=100)
    alamat = forms.CharField(widget=forms.Textarea)
    gender = forms.CharField(max_length=100)
    tanggal_lahir = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    no_hp = forms.CharField(max_length=100)
    panjang_tarikan = forms.CharField(max_length=100)
    posisi = forms.CharField(max_length=100)
    picture = forms.ImageField()

    class Meta:
        model = Anggota
