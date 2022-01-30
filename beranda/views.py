import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from staf_pegawai.models import Akun, Pegawai, Jabatan
from django.contrib import messages
from beranda import auth
from django.contrib.auth.decorators import login_required
from presensi_manual.models import Log
from presensi_manual.models import Absensi
from django.conf import settings
from django.db.models import Count
import pandas as pd
# Create your views here.

# landing page
def home(request):
	context = {
		'title':'home',
		'heading':'halaman home',
	}
	return render(request, 'beranda/home.html', context)

def about(request):
    context = {
        'title':'about',
        'heading':'halaman about',
    }
    return render(request, 'beranda/about.html', context)

def contact(request):
    context = {
        'title':'contact',
        'heading':'CONTACT US',
    }
    return render(request, 'beranda/contact.html', context)


def layanan_service(request):
    context = {
        'title':'layanan service',
        'heading':''
    }
    return render(request, 'beranda/layanan_service.html', context)

def FAQ(request):
    context = {
        'title':'FAQ',
        'heading':''
    }
    return render(request, 'beranda/FAQ.html', context)

def login_view(request):
    context = {
        'page_title' : 'Presensi Pegawai Diskominfo'
    }

    # if request.GET:
    #     if request.user.is_authenticated():
    #         return redirect('dashboard')
    #     else:
    #         return render(request, 'login.html', context)


    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                try:
                    akun = Akun.objects.get(akun=user.id)
                    login(request, user)
                    request.session['pegawai_id'] = akun.pegawai.id
                    request.session['jenis_akun'] = akun.jenis_akun
                    request.session['username'] = request.POST['username']
                    messages.success(request, "list staf pegawai success update!!")
                    return redirect('/dashboard')
                except:
                    messages.add_message(request, messages.INFO,
                                         'Akun ini belum terhubung dengan data pegawai, silahkan hubungi administrator')
            else:
                messages.add_message(request, messages.INFO, 'User belum terverifikasi')
        else:
            messages.add_message(request, messages.INFO, 'Username atau password Anda salah')
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('/login/')

#schedule staf_pegawai
def schedule(request):
    context = {
        'title':'schedule',
        'heading':'halaman jadwal',
    }
    return render(request, 'beranda/schedule.html', context)


# dashboard pegawai
@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    
    c_hadir = Absensi.objects.filter(status='hadir') \
        .annotate(created_count=Count('pegawai_id')) \
        .exclude(pegawai_id=0).count()

    c_alpa = Absensi.objects.filter(status='alpa') \
        .annotate(created_count=Count('pegawai_id')) \
        .exclude(pegawai_id=0).count()

    c_sakit = Absensi.objects.filter(status='sakit') \
        .annotate(created_count=Count('pegawai_id')) \
        .exclude(pegawai_id=0).count()

    c_ijin = Absensi.objects.filter(status='ijin') \
        .annotate(created_count=Count('pegawai_id')) \
        .exclude(pegawai_id=0).count()

    c_absen = [c_hadir, c_ijin, c_sakit, c_alpa]

    return render(request, 'dashboard/pegawai_dashboard.html', {'c_absen': c_absen})


def visualisasi(request):


    c_hadir = Absensi.objects.filter(status='hadir') \
        .annotate(created_count=Count('pegawai_id')) \
        .exclude(pegawai_id=0).count() 

    c_alpa = Absensi.objects.filter(status='alpa') \
        .annotate(created_count=Count('pegawai_id')) \
        .exclude(pegawai_id=0).count()

    c_sakit = Absensi.objects.filter(status='sakit') \
        .annotate(created_count=Count('pegawai_id')) \
        .exclude(pegawai_id=0).count()

    c_ijin = Absensi.objects.filter(status='ijin') \
        .annotate(created_count=Count('pegawai_id')) \
        .exclude(pegawai_id=0).count()

    data = [c_hadir, c_sakit, c_ijin, c_alpa]

    labels = [c_hadir, c_sakit, c_ijin, c_alpa]

    c_absen = [c_hadir, c_ijin, c_sakit, c_alpa]
    
    # item=Absensi.objects.all()[:4].values()
    # df=pd.DataFrame(item)
    # hadir=df.status.tolist()
    # alpa=df.status.tolist()
    # sakit=df.status.tolist()
    # ijin=df.status.tolist()
    # df=df['pegawai_id'].tolist()
    # mydict={
    #     'df':df,
    #     'hadir':hadir,
    #     'alpa':alpa,
    #     'sakit':sakit,
    #     'ijin':ijin,
    # }
    # labels = []
    # data = []

    # queryset = Absensi.objects.order_by('status')[:4]
    # for person in queryset:
    #     labels.append(person.pegawai_id)
    #     data.append(person.status)

    
    return render(request, 'dashboard/visualisasi.html', {
        'labels': labels,
        'data': data,
        'c_absen': c_absen,
    })
        

def profile(request):
    context = {}
    return render(request, 'dashboard/profile.html', context)