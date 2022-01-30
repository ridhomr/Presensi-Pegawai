"""myface URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from beranda import views as page_beranda
from staf_pegawai import views
from golongan import views
from file_upload.views import upload
from beranda.views import login_view
#from presensi_manual.views import presensi
from presensi_face.views import presensi_face
from report.views import *


urlpatterns = [
    path('dashboard/pegawai/', include('staf_pegawai.urls')),
    path('presensi_manual/', include('presensi_manual.urls')),
    path('dashboard/golongan/', include('golongan.urls')),
    path('dashboard/feedback/', include('feedback.urls')),
    path('report/', include('report.urls')),
    path('',  page_beranda.home, name='home'),
    path('about/',  page_beranda.about, name='about'),
    path('contact/', page_beranda.contact, name='contact'),
    path('layanan-service/', page_beranda.layanan_service, name='layanan_service'),
    path('FAQ/', page_beranda.FAQ, name='FAQ'),
    path('schedule/',  page_beranda.schedule, name='schedule'),
    path('admin/', admin.site.urls),
    path('login/', page_beranda.login_view, name='login'),
    path('logout/', page_beranda.logout_view,name='logout_view'),
    path('dashboard/', page_beranda.dashboard, name='dashboard'),
    path('dashboard/upload/', upload, name="uploaded"),
    path('dashboard/visualisasi/',  page_beranda.visualisasi, name='visualisasi'),
    path('dashboard/profile/', page_beranda.profile, name="profile"),
    # path('dashboard/presensi-manual/', presensi, name="presensi_manual"),
    path('dashboard/presensi-face/', presensi_face, name="presensi_face"),
    # path('dashboard/jabatan/', views.jabatan, name="hak_akses"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
