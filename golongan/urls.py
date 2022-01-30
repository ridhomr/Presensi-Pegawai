from django.urls import path
from . import views

urlpatterns = [
	path('', views.golongan_form, name='tambah_golongan'),
	path('<int:id>/', views.golongan_form,  name='ubah_golongan'),
	path('delete/<int:id>/', views.golongan_delete, name='hapus_golongan'),
	path('list/', views.golongan_list, name='tampil_golongan'),
]