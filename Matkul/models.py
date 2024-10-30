from django.db import models

# Create your models here.
class Matkul(models.Model):
    nama_matkul = models.CharField(max_length=120, null=True)
    jurusan = models.CharField(max_length=20, null=True)
 