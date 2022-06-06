from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Contacto_formulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    correo = forms.EmailField()
    asunto = forms.CharField(max_length=250)
    mensaje = forms.CharField(widget=forms.Textarea)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {parameters: '' for parameters in fields }
