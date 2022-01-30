from django.urls import path
from . import views

urlpatterns = [
    path('',views.laporan_form),
    path('list/', views.laporan_list, name="laporan_index"),
]
