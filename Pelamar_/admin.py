from django.contrib import admin
from .models import Pelamar, Posisi, Wawancara, Status

# ModelAdmin untuk Pelamar
@admin.register(Pelamar)
class PelamarAdmin(admin.ModelAdmin):
    list_display = ('id_pelamar', 'nama', 'email', 'nomor_telepon', 'tanggal_melamar')
    search_fields = ('nama', 'email', 'nomor_telepon')
    list_filter = ('tanggal_melamar',)
    ordering = ('-tanggal_melamar',)


# ModelAdmin untuk Posisi
@admin.register(Posisi)
class PosisiAdmin(admin.ModelAdmin):
    list_display = ('id_posisi', 'nama_posisi', 'tanggal_dibuka', 'tanggal_ditutup')
    search_fields = ('nama_posisi',)
    list_filter = ('tanggal_dibuka', 'tanggal_ditutup')
    ordering = ('-tanggal_dibuka',)


# ModelAdmin untuk Wawancara
@admin.register(Wawancara)
class WawancaraAdmin(admin.ModelAdmin):
    list_display = ('id_wawancara', 'pelamar', 'posisi', 'tanggal_wawancara', 'hasil_wawancara')
    search_fields = ('pelamar__nama', 'posisi__nama_posisi')
    list_filter = ('tanggal_wawancara', 'hasil_wawancara')
    ordering = ('-tanggal_wawancara',)
    autocomplete_fields = ('pelamar', 'posisi')


# ModelAdmin untuk Status
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id_status', 'pelamar', 'status_rekrutmen')
    search_fields = ('pelamar__nama', 'status_rekrutmen')
    list_filter = ('status_rekrutmen',)
    ordering = ('-id_status',)
    autocomplete_fields = ('pelamar',)
