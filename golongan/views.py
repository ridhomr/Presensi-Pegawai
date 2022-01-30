from django.shortcuts import render, redirect
from staf_pegawai.models import Golongan
from .forms import GolonganForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def golongan_list(request):
	context = {'daftar_golongan': Golongan.objects.all()}
	return render(request, 'dashboard/golongan_list.html', context)

@login_required(login_url=settings.LOGIN_URL)
def golongan_form(request, id=0):
	if request.method == "POST":
		if id  == 0:
			form = GolonganForm(request.POST)
		else:
			glg = Golongan.objects.get(pk=id)
			form = GolonganForm(request.POST, instance=glg)
		form.save()
		return redirect('/dashboard/golongan/list')

	else:
		if id == 0:
			form = GolonganForm()
		else:
			glg = Golongan.objects.get(pk=id)
			form = GolonganForm(instance=glg)
		return render(request, "dashboard/golongan_form.html", {'form': form})

@login_required(login_url=settings.LOGIN_URL)
def golongan_delete(request, id):
	glg = Golongan.objects.get(pk=id)
	glg.delete()
	return redirect('/dashboard/golongan/list')