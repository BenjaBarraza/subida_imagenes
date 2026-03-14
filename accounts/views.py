from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Auto-login tras registro exitoso
            messages.success(request, f"¡Cuenta creada con éxito! Bienvenido, {user.username}.")
            return redirect('upload_panel') # Redirige al panel
        else:
            messages.error(request, "Por favor, corrige los errores del formulario.")
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})