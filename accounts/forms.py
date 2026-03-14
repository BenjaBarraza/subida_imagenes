from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroProForm(UserCreationForm):
    # Añadimos el correo electrónico como obligatorio
    email = forms.EmailField(
        required=True, 
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'placeholder': 'tu@correo.com'})
    )
    
    # Añadimos el checkbox de términos
    terms = forms.BooleanField(
        required=True,
        label="Acepto los Términos y Condiciones de la plataforma"
    )

    class Meta:
        model = User
        # Ordenamos cómo queremos que aparezcan los campos
        fields = ("username", "email") 
        # (Django añade automáticamente las dos contraseñas al heredar de UserCreationForm)



# --- Formulario de login personalizado ---
class LoginProForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'placeholder': 'tu@correo.com'})
    )
    password = forms.CharField(
        required=True,
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••'})
    )