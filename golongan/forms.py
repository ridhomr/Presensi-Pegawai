from django import forms
from staf_pegawai.models import Golongan

class GolonganForm(forms.ModelForm):
	class Meta:
		model = Golongan
		fields = '__all__'