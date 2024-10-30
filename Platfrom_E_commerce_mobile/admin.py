from django.contrib import admin

from Konsumen.models import Konsumen
from Member.models import Member
from Admin.models import Admin
from Keranjang.models import Keranjang
from Pesan.models import Pesan
from Admin.models import Admin
from Laporan.models import Laporan
from Transaksi.models import Transaksi
from Produk.models import Produk


# Admin untuk Konsumen
class KonsumenAdmin(admin.ModelAdmin):
    list_display = ('nama_konsumen', 'email', 'nomor_telepon', 'tanggal_registrasi')
    search_fields = ('nama_konsumen', 'email')
    list_filter = ('tanggal_registrasi',)
    ordering = ('-tanggal_registrasi',)

admin.site.register(Konsumen,KonsumenAdmin)

# Admin untuk Member
class MemberAdmin(admin.ModelAdmin):
    list_display = ('nama_member', 'email', 'status_member', 'tanggal_bergabung')
    search_fields = ('nama_member', 'email')
    list_filter = ('status_member', 'tanggal_bergabung')
    ordering = ('-tanggal_bergabung',)
admin.site.register(Member,MemberAdmin)

# Admin untuk Produk
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('nama_produk', 'kategori_produk', 'harga_produk', 'stok_produk', 'tanggal_ditambahkan')
    search_fields = ('nama_produk', 'kategori_produk')
    list_filter = ('kategori_produk', 'tanggal_ditambahkan')
    ordering = ('-tanggal_ditambahkan',)
admin.site.register(Produk,ProdukAdmin)

# Admin untuk Transaksi
class TransaksiAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'tanggal_transaksi', 'total_harga', 'metode_pembayaran', 'status_pembayaran')
    search_fields = ('member__nama_member',)
    list_filter = ('metode_pembayaran', 'status_pembayaran', 'tanggal_transaksi')
    ordering = ('-tanggal_transaksi',)
admin.site.register(Transaksi,TransaksiAdmin)

# Admin untuk Keranjang
class KeranjangAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'produk', 'jumlah_produk', 'tanggal_ditambahkan')
    search_fields = ('member__nama_member', 'produk__nama_produk')
    list_filter = ('tanggal_ditambahkan',)
    ordering = ('-tanggal_ditambahkan',)
admin.site.register(Keranjang,KeranjangAdmin)

# Admin untuk Pesan
class PesanAdmin(admin.ModelAdmin):
    list_display = ('id', 'pengirim', 'admin', 'tanggal_kirim',)
    search_fields = ('pengirim__nama_member', 'admin__nama_admin',)
    list_filter = ('tanggal_kirim',)
    ordering = ('-tanggal_kirim',)

admin.site.register(Pesan,PesanAdmin)


# Admin untuk Admin
class AdminAdmin(admin.ModelAdmin):
    list_display = ('nama_admin', 'email_admin', 'jabatan', 'tanggal_bergabung')
    search_fields = ('nama_admin', 'email_admin')
    list_filter = ('jabatan', 'tanggal_bergabung')
    ordering = ('-tanggal_bergabung',)
admin.site.register(Admin,AdminAdmin)

# Admin untuk Laporan
class LaporanAdmin(admin.ModelAdmin):
    list_display = ('id', 'jenis_laporan', 'admin', 'tanggal_laporan')
    search_fields = ('jenis_laporan', 'admin__nama_admin')
    list_filter = ('jenis_laporan', 'tanggal_laporan')
    ordering = ('-tanggal_laporan',)
admin.site.register(Laporan,LaporanAdmin)
