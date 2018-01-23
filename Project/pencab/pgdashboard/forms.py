from django import forms
from orm.models import PenCab

class PenCabForm(forms.Form):
    
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    name = forms.CharField(max_length=100)
    
    class Meta:
        model = PenCab