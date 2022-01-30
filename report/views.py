from django.shortcuts import render, redirect
from datetime import datetime, date
from presensi_manual.models import Log, Absensi
from report.forms import LogForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from presensi_manual.models import Absensi

# Create your views here.
def laporan_form(request):
	form = LogForm()
	context = {
		'form':form
	}

	if request.method == 'POST':
		form = LogForm(request.POST)
		form.save()
		return redirect('/report/list')
	else:
		return render(request, 'report/report_form.html', context)

# def laporan(request):
#     if request.method == 'POST':
#         tanggal = request.POST['tanggal']
#         tgl = "{}".format(tanggal).split('-')
#         y = int(tgl[0])
#         m = int(tgl[1])
#         d = int(tgl[2])
#         dt = datetime(year=y, month=m, day=d)
#         logs = Log.objects.filter(waktu_masuk__date=dt).order_by('waktu_masuk').exclude(pegawai_id=0)
#     else:
#         logs = Log.objects.filter(waktu_masuk__date=date.today()).order_by('waktu_masuk').exclude(pegawai_id=0)
#     return render(request, 'report/report.html', {'active': 'laporan', 'data': logs})

@login_required(login_url=settings.LOGIN_URL)
def laporan_list(request):
	context = {
		'daftar_presensi': Absensi.objects.all()
	}

	# pegawai=Pegawai.objects.get(roll_no=request.id)
	# bor=Borrower.objects.filter(pegawai=Pegawai)
	# list=[]
	# for prs in bor:
	# 	list.append(b.pegawai)
	return render(request, 'report/report.html', context)