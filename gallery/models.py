from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=150, blank=True, verbose_name="Título")
    image = models.ImageField(upload_to='pics/', verbose_name="Archivo de Imagen")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Imagen {self.id}"