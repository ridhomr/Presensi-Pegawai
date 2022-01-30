from django.shortcuts import render, redirect, get_object_or_404
from .forms import PegawaiForm, JabatanForm
from .models import Jabatan, Pegawai
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def pegawai_list(request):
	context = {
		'daftar_pegawai': Pegawai.objects.all()
	}
	return render(request, 'dashboard/pegawai_list.html', context)

@login_required(login_url=settings.LOGIN_URL)
def pegawai_form(request, id=0):
	# untuk proses update
	if request.method == "POST":
		if id == 0:
			form = PegawaiForm(request.POST)
		else:
			pwg = Pegawai.objects.get(pk=id)
			form = PegawaiForm(request.POST, instance=pwg)
		form.save()
		messages.success(request, "Hello selamat datang di Myface Diskominfo Kab. Mempawah!!")
		return redirect('/dashboard/pegawai/list')

	# untuk proses insert
	else:
		if id == 0:
			form = PegawaiForm()
		else:
			pwg = Pegawai.objects.get(pk=id)
			form = PegawaiForm(instance=pwg)
		return render(request, 'dashboard/pegawai_form.html', {'form': form})

# delete list pegawai
@login_required(login_url=settings.LOGIN_URL)
def pegawai_delete(request, id):
	pwg = Pegawai.objects.get(pk=id)
	pwg.delete()
	messages.success(request, "data pegawai berhasil dihapus")
	return redirect('/dashboard/pegawai/list')


# list jabatan
def jabatan(request):
	context = {'daftar_jabatan': Jabatan.objects.all()}
	return render(request, 'dashboard/jabatan_list.html', context)

