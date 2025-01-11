# Generated by Django 5.1.1 on 2025-01-11 05:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelamar',
            fields=[
                ('id_pelamar', models.AutoField(primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=100)),
                ('alamat', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nomor_telepon', models.CharField(max_length=15)),
                ('cv', models.FileField(blank=True, null=True, upload_to='cv/')),
                ('tanggal_melamar', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posisi',
            fields=[
                ('id_posisi', models.AutoField(primary_key=True, serialize=False)),
                ('nama_posisi', models.CharField(max_length=100)),
                ('deskripsi', models.TextField()),
                ('kualifikasi', models.TextField()),
                ('tanggal_dibuka', models.DateField()),
                ('tanggal_ditutup', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id_status', models.AutoField(primary_key=True, serialize=False)),
                ('status_rekrutmen', models.CharField(choices=[('Dalam Proses', 'Dalam Proses'), ('Lulus', 'Lulus'), ('Tidak Lulus', 'Tidak Lulus'), ('Diterima', 'Diterima')], max_length=50)),
                ('catatan', models.TextField(blank=True, null=True)),
                ('pelamar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='Sistem_Rekrutme_Karyawan.pelamar')),
            ],
        ),
        migrations.CreateModel(
            name='Wawancara',
            fields=[
                ('id_wawancara', models.AutoField(primary_key=True, serialize=False)),
                ('tanggal_wawancara', models.DateField()),
                ('hasil_wawancara', models.CharField(blank=True, choices=[('Lulus', 'Lulus'), ('Tidak Lulus', 'Tidak Lulus')], max_length=50, null=True)),
                ('komentar_pewawancara', models.TextField(blank=True, null=True)),
                ('pelamar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wawancara', to='Sistem_Rekrutme_Karyawan.pelamar')),
                ('posisi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wawancara', to='Sistem_Rekrutme_Karyawan.posisi')),
            ],
        ),
    ]
