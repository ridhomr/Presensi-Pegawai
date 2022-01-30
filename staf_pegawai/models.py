from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Jabatan(models.Model):
    nama = models.CharField(max_length=50)

    def __str__(self):
        return self.nama


class Pegawai(models.Model):
    JENIS_KELAMIN = (
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan')
    )
    nip = models.CharField(max_length=18, unique=True)
    nama = models.CharField(max_length=255)
    tgl_lahir = models.DateField()
    alamat = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN)
    no_hp = models.CharField(max_length=15, unique=True)
    jabatan = models.ForeignKey(Jabatan, null=True, related_name='pegawai', on_delete=models.SET_NULL)

    def __str__(self):
        return self.nip


class Akun(models.Model):
    JENIS_AKUN_CHOICES = (
        ('pegawai', 'Pegawai'),
        ('admin', 'Administrator'),
    )
    akun = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    pegawai = models.ForeignKey(Pegawai, null=True, on_delete=models.SET_NULL)
    jenis_akun = models.CharField(max_length=20, choices=JENIS_AKUN_CHOICES)

    def __str__(self):
        return str(self.pegawai)

class Golongan(models.Model):
    GOLONGAN = (
        ('PNS', 'Pegawai Negeri Sipil'),
        ('Cleaning Service', 'Cleaning Service'),
        ('Staf Administratip bagian rumah sakit', 'staf'),
        ('CPNS','CPNS'),
        ('Staf RSUD','Staf RSUD'),
        ('Penjaga Malam', 'Penjaga Malam'),
        ('Persandian','Persandian'),
        ('Operator Telepon','Operator Telepon'),
        ('Regu Pagi','Regu Pagi'),
        ('Regu Siang','Regu Siang'),
        ('Regu Malam','Regu Malam'),
    )
    pegawai = models.ForeignKey(Pegawai, null=True, on_delete=models.SET_NULL)
    golongan = models.CharField(max_length=150, choices=GOLONGAN)

    def __str__(self):
        return str(self.pegawai)

class Feedback(models.Model):
    FEEDBACK = (
        ('Sangat_Puas', 'Sangat_Puas'),
        ('Puas', 'Puas'),
        ('Cukup', 'Cukup'),
        ('Tidak_Puas', 'Tidak_Puas'),
        ('Sangat_Buruk', 'Sangat_Buruk')
    )
    pegawai = models.ForeignKey(Pegawai, null=True, on_delete=models.SET_NULL)
    rating_score = models.CharField(max_length=200, choices=FEEDBACK)
    masukkan = models.TextField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return str(self.pegawai)