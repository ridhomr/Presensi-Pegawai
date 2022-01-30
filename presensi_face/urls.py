from django.urls import path 
from . import views

urlpatterns = [
	path('', presensi, name="presensi_manual"),
]