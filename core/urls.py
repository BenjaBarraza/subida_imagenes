from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Delegamos las rutas a sus respectivas apps
    path('auth/', include('accounts.urls')), 
    path('', include('gallery.urls')),
]

# Muy importante: esto permite ver las imágenes en el navegador durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)