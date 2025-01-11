from django.db import models
from django.db import models

# Model Pelamar
class Pelamar(models.Model):
    id_pelamar = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    email = models.EmailField(unique=True)
    nomor_telepon = models.CharField(max_length=15)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    tanggal_melamar = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nama


# Model Posisi
class Posisi(models.Model):
    id_posisi = models.AutoField(primary_key=True)
    nama_posisi = models.CharField(max_length=100)
    deskripsi = models.TextField()
    kualifikasi = models.TextField()
    tanggal_dibuka = models.DateField()
    tanggal_ditutup = models.DateField()

    def __str__(self):
        return self.nama_posisi


# Model Wawancara
class Wawancara(models.Model):
    id_wawancara = models.AutoField(primary_key=True)
    pelamar = models.ForeignKey(Pelamar, on_delete=models.CASCADE, related_name='wawancara')
    posisi = models.ForeignKey(Posisi, on_delete=models.CASCADE, related_name='wawancara')
    tanggal_wawancara = models.DateField()
    hasil_wawancara = models.CharField(max_length=50, choices=[
        ('Lulus', 'Lulus'),
        ('Tidak Lulus', 'Tidak Lulus'),
    ], blank=True, null=True)
    komentar_pewawancara = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Wawancara {self.pelamar.nama} untuk {self.posisi.nama_posisi}"


# Model Status
class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    pelamar = models.OneToOneField(Pelamar, on_delete=models.CASCADE, related_name='status')
    status_rekrutmen = models.CharField(max_length=50, choices=[
        ('Dalam Proses', 'Dalam Proses'),
        ('Lulus', 'Lulus'),
        ('Tidak Lulus', 'Tidak Lulus'),
        ('Diterima', 'Diterima'),
    ])
    catatan = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Status {self.pelamar.nama}: {self.status_rekrutmen}"

# Create your models here.
