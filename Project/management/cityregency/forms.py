from django import forms
from orm.models import CityRegency
from orm.models import Province

class CityRegencyForm(forms.Form):
    
    id = forms.CharField(required=False, widget=forms.HiddenInput())
    name = forms.CharField(max_length=100)
    province_all = Province.objects.all()
    province = forms.ModelChoiceField(queryset=province_all, initial=0) 
    
    class Meta:
        model = CityRegency