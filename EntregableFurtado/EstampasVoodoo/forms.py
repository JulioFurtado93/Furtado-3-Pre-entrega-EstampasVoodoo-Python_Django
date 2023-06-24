from django import forms

class formSetCliente(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    telefono = forms.IntegerField()
    email = forms.EmailField()