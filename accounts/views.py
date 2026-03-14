from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistroProForm, LoginProForm 

def register_view(request):
    if request.method == 'POST':
        form = RegistroProForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # ELIMINAMOS EL AUTO-LOGIN
            # login(request, user) <--- Esto ya no va
            
            # Cambiamos el mensaje para que sepa que tiene que loguearse
            messages.success(request, "¡Cuenta creada con éxito! Por favor, inicia sesión con tu nuevo correo.")
            
            # Redirigimos al Login en lugar de al panel de subida
            return redirect('accounts:login')
    else:
        form = RegistroProForm()
    
    return render(request, 'accounts/register.html', {'form': form})

# --- EL LOGIN SE QUEDA IGUAL ---
def login_view(request):
    if request.method == 'POST':
        form = LoginProForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            user_obj = User.objects.filter(email=email).first()
            
            if user_obj:
                user = authenticate(request, username=user_obj.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"¡Bienvenido de nuevo!")
                    return redirect('upload_panel')
                else:
                    messages.error(request, "Contraseña incorrecta.")
            else:
                messages.error(request, "No existe ninguna cuenta registrada con este correo.")
    else:
        form = LoginProForm()
        
    return render(request, 'accounts/login.html', {'form': form})