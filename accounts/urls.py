from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts' # Namespace para evitar choques de nombres

urlpatterns = [
    # Usamos las vistas nativas de Django, pero le decimos dónde buscar el HTML
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='gallery_index'), name='logout'),
    
    # Nuestra vista personalizada de registro
    path('registro/', views.register_view, name='register'),
]