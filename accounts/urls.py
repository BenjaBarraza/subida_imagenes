from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts' # Namespace para evitar choques de nombres

urlpatterns = [
    # Usamos NUESTRA vista personalizada para el Login (así permite correo electrónico)
    path('login/', views.login_view, name='login'),
    
    # El Logout lo seguimos manejando con la vista nativa de Django porque funciona perfecto
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),

    # Nuestra vista personalizada de registro (la que pide correo y términos)
    path('registro/', views.register_view, name='register'),
]