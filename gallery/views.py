from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from django.contrib import messages

# Solo para ver
def gallery_view(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery/index.html', {'photos': photos})

# Solo para gestionar (subir/ver lista de borrado)
def upload_view(request):
    if request.method == 'POST' and request.FILES.get('image_file'):
        image = request.FILES['image_file']
        title = request.POST.get('title', '')
        Photo.objects.create(title=title, image=image)
        messages.success(request, "¡Imagen subida con éxito!") # <--- Mensaje
        return redirect('upload_panel')

    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery/upload.html', {'photos': photos})

def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.image.delete()
    photo.delete()
    messages.warning(request, "Imagen eliminada correctamente.") # <--- Mensaje
    return redirect('upload_panel')
