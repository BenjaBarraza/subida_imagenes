from django.urls import path
from .views import gallery_view, upload_view, delete_photo

urlpatterns = [
    path('', upload_view, name='upload_panel'),          # Ahora esta es la raíz (http://127.0.0.1:8000/)
    path('ver/', gallery_view, name='gallery_index'),    # La galería pasa a /ver/
    path('delete/<int:pk>/', delete_photo, name='delete_photo'),
]