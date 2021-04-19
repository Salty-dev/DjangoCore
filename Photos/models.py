from django.db import models
from django.db.models.signals import post_delete

from pathlib import Path


class Category(models.Model):
    name = models.CharField("Név", max_length=100)

    class Meta:
        verbose_name_plural = "Kategóriák"

    def __str__(self):
        return self.name


class Photo(models.Model):
    name = models.CharField("Cím", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photos")
    description = models.TextField()
    uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Fotók"

    def __str__(self):
        return self.name


def file_cleanup(sender, instance, **kwargs):
    Path(instance.image.path).unlink()


post_delete.connect(file_cleanup, sender=Photo)
