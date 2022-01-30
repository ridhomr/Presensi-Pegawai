from django.urls import path 
from . import views

urlpatterns = [
	#path('', presensi, name="presensi_manual"),
	path('', views.presensi_form, name="tambah_presensi"),
	path('<int:id>/', views.presensi_form, name="ubah_presensi"),
	path('list/', views.presensi_list, name="tampil_presensi"),
	path('delete/<int:id>', views.presensi_delete, name="hapus_presensi"),
]