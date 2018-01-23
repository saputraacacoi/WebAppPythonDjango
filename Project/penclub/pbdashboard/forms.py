from django import forms
from orm.models import CityRegency, Club, ClubFiles


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