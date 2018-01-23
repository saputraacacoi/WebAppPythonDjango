from django import forms
from orm.models import Club
from orm.models import CityRegency

class ClubForm(forms.Form):
    
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    name = forms.CharField(max_length=100)
    register_number = forms.CharField(max_length=100)
    since = forms.CharField(max_length=100)
    secretariat = forms.CharField(max_length=100)
    leader = forms.CharField(max_length=100)
    slogan = forms.CharField(widget=forms.Textarea)
    cityregency_all = CityRegency.objects.all()
    cityregency = forms.ModelChoiceField(queryset=cityregency_all, initial=0) 
    
    class Meta:
        model = Club