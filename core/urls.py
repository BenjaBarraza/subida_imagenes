from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Delegamos las rutas a sus respectivas apps
    path('auth/', include('accounts.urls')), 
    path('', include('gallery.urls')),
]