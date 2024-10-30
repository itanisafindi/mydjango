from django.db import models

# Create your models here.
class prodi(models.Model):
    nama = models.CharField(max_length=100, null=True)
    kode = models.CharField(max_length=5, null=True)

        