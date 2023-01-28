from django import forms
from .models import *

class ProductForm(forms.Form):
    optioncolor = (('สีดำ','สีดำ'),('สีขาว', 'สีขาว'), ('สีแดง', 'สีแดง'),('สีชมพู', 'สีชมพู'))
    optionpro = (('มี', 'มี'),('ไม่มี', "ไม่มี"))
    pid = forms.CharField()
    pname = forms.CharField()
    colors = forms.ChoiceField(widget=forms.Select, choices= optioncolor, initial='สีดำ')
    size = forms.CharField()
    price = forms.IntegerField(min_value=0)
    amount = forms.IntegerField(min_value=0)
    promotion = forms.ChoiceField(widget=forms.RadioSelect,choices=optionpro)
