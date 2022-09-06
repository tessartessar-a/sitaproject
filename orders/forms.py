from attr import field
from django import forms
from django.forms import ModelForm
from .models import Data, Status



#Create Data Form

class DataForm(ModelForm): 
    class Meta: 
        model = Data
        fields = ('in_date','name_customer','jobs','out_date', 'upload')

        widget = { 
            'in_date': forms.DateInput(attrs={'class':'form-control'}),
            'name_customer': forms.TextInput(attrs={'class':'form-control'}),
            'jobs': forms.Select(attrs={'class':'form-control'}),
            'out_date': forms.DateInput(attrs={'class':'form-control'}),
            'upload': forms.TextInput(attrs={'class':'form-control'}),
        }