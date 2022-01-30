from django.db import models
from staf_pegawai.models import Pegawai
from datetime import date
# Create your models here.

class Log(models.Model):
    CHOICES = (
        ('H', 'Hadir'), 
        ('A', 'Tanpa Keterangan'), 
        ('I', 'Ijin'), 
        ('S','Sakit')
    )

    pegawai = models.ForeignKey(Pegawai, related_name='log', blank=True, on_delete=models.CASCADE)
    keterangan = models.CharField(max_length=200)
    status = models.CharField(max_length=1, choices=CHOICES, default='H')
    waktu_masuk = models.DateTimeField(auto_now=False)
    waktu_keluar = models.DateTimeField(auto_now=False, blank=True)

    # def __str__(self):
    #     return  self.pegawai
    def __str__(self):
        return "{}/{}/{} {}:{} - {} {}".format(self.waktu_masuk.day, self.waktu_masuk.month, self.waktu_masuk.year, self.waktu_masuk.hour,
                                               self.waktu_masuk.minute, self.pegawai.nip,
                                               self.pegawai.nama)


class Absensi(models.Model):
    CHOICES = (
        ('hadir', 'hadir'), 
        ('alpa', 'alpa'), 
        ('ijin', 'ijin'), 
        ('sakit','sakit')
    )
    pegawai = models.ForeignKey(Pegawai, related_name='absensi', blank=False, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=CHOICES)
    keterangan = models.CharField(max_length=200)
    last_update = models.DateField(auto_now=True)
    last_update_time = models.TimeField(auto_now=True)
    def __str__(self):
        return self.pegawai.nip