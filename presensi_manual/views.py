from django.shortcuts import render, redirect, get_object_or_404
from .forms import PresensiForm
from .models import Absensi
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from staf_pegawai.models import Pegawai

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def presensi_list(request):
	context = {
		'daftar_presensi': Absensi.objects.all()
	}

	# pegawai=Pegawai.objects.get(roll_no=request.id)
	# bor=Borrower.objects.filter(pegawai=Pegawai)
	# list=[]
	# for prs in bor:
	# 	list.append(b.pegawai)
	return render(request, 'presensi_manual/presensi_manual_list.html', context)

@login_required(login_url=settings.LOGIN_URL)
def presensi_form(request, id=0):
	form = PresensiForm()
	context = {
		'form':form
	}

	if request.method == "POST":
		if id  == 0:
			form = PresensiForm(request.POST)
		else:
			prs = Absensi.objects.get(pk=id)
			form = PresensiForm(request.POST, instance=prs)
		form.save()
		messages.success(request, "Presensi sukses di update!!")
		return redirect('/presensi_manual/list')

	else:
		if id  == 0:
			form = PresensiForm()
		else:
			prs = Absensi.objects.get(pk=id)
			form = PresensiForm(instance=prs)
		return render(request, "presensi_manual/presensi_manual_form.html", {'form': form})

@login_required(login_url=settings.LOGIN_URL)
def presensi_delete(request, id):
	prs = Absensi.objects.get(pk=id)
	prs.delete()
	messages.success(request, "Presensi berhasil dihapus!!")
	return redirect('/presensi_manual/list')