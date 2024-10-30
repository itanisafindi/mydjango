from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

# Entitas Konsumen
class Konsumen(models.Model):
    nama_konsumen = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    alamat = models.TextField(blank=True, null=True)
    nomor_telepon = models.CharField(max_length=15, blank=True, null=True)
    tanggal_registrasi = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nama_konsumen

# Entitas Member
class Member(models.Model):
    STATUS_CHOICES = [
        ('Aktif', 'Aktif'),
        ('Nonaktif', 'Nonaktif'),
    ]
    nama_member = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    alamat = models.TextField(blank=True, null=True)
    nomor_telepon = models.CharField(max_length=15, blank=True, null=True)
    status_member = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Aktif')
    tanggal_bergabung = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nama_member

# Entitas Produk
class Produk(models.Model):
    nama_produk = models.CharField(max_length=100)
    deskripsi_produk = models.TextField(blank=True, null=True)
    kategori_produk = models.CharField(max_length=50, blank=True, null=True)
    harga_produk = models.DecimalField(max_digits=10, decimal_places=2)
    stok_produk = models.IntegerField()
    tanggal_ditambahkan = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nama_produk

# Entitas Transaksi
class Transaksi(models.Model):
    METODE_PEMBAYARAN_CHOICES = [
        ('Transfer', 'Transfer'),
        ('Kartu Kredit', 'Kartu Kredit'),
        ('COD', 'COD'),
    ]
    STATUS_PEMBAYARAN_CHOICES = [
        ('Lunas', 'Lunas'),
        ('Belum Lunas', 'Belum Lunas'),
    ]
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='transaksi')
    tanggal_transaksi = models.DateField(default=timezone.now)
    total_harga = models.DecimalField(max_digits=10, decimal_places=2)
    metode_pembayaran = models.CharField(max_length=15, choices=METODE_PEMBAYARAN_CHOICES)
    status_pembayaran = models.CharField(max_length=15, choices=STATUS_PEMBAYARAN_CHOICES)

    def __str__(self):
        return f"Transaksi {self.id} - {self.member.nama_member}"

# Entitas Keranjang
class Keranjang(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='keranjang')
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE, related_name='keranjang')
    jumlah_produk = models.IntegerField()
    tanggal_ditambahkan = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Keranjang {self.member.nama_member} - {self.produk.nama_produk}"

# Entitas Pesan
class Pesan(models.Model):
    pengirim = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='pesan', null=True)
    admin = models.ForeignKey('Admin', on_delete=models.SET_NULL, null=True, related_name='pesan')
    isi_pesan = models.TextField()
    tanggal_kirim = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Pesan dari {self.pengirim.nama_member if self.pengirim else 'Konsumen'}"

# Entitas Admin
class Admin(models.Model):
    nama_admin = models.CharField(max_length=100)
    email_admin = models.EmailField(unique=True)
    jabatan = models.CharField(max_length=50, blank=True, null=True)
    tanggal_bergabung = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nama_admin

# Entitas Laporan
class Laporan(models.Model):
    jenis_laporan = models.CharField(max_length=50)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='laporan')
    tanggal_laporan = models.DateField(default=timezone.now)
    isi_laporan = models.TextField()

    def __str__(self):
        return f"Laporan {self.jenis_laporan} - {self.admin.nama_admin}"
