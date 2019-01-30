from django import forms
from .models import *

class OperatorForm(forms.ModelForm):
    class Meta:
         model=Operators

         fields = [
             'country'
             'operator_name',
             'operator_description',
             'image'
         ]

