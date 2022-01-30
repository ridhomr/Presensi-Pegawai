from django.urls import path 
from . import views

urlpatterns = [
	path('', views.pegawai_form, name="pegawai_form"),
	path('<int:id>/',  views.pegawai_form, name="ubah_pegawai"),
	path('delete/<int:id>/', views.pegawai_delete, name="hapus_pegawai"),
	path('list/', views.pegawai_list, name="pegawai_list"),
	path('dashboard/jabatan/', views.jabatan, name="jabatan"),
]

