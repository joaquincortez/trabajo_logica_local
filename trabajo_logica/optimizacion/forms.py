from django import forms

class CalculosForm(forms.Form):
    sabor_helado = forms.CharField(label='Sabor helado', max_length=100)