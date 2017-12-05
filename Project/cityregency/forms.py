from django import forms
from orm.models import CityRegency

class CityRegencyForm(forms.Form):
    
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    name = forms.CharField(max_length=100)
    
    class Meta:
        model = CityRegency