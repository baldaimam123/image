from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    judul = models.CharField(max_length=255)
    body = models.TextField()
    category = models.CharField(max_length=255)
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True)
    foto = models.ImageField(upload_to="info-harga/foto")  # Gunakan ImageField

    def save(self, *args, **kwargs):
        self.slug = slugify(self.judul)
        super().save(*args, **kwargs)

    def __str__(self):
        return "{}.{}".format(self.id, self.judul)
