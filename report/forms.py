from django import forms
from presensi_manual.models import Log

class  LogForm(forms.ModelForm):
	class Meta:
		model = Log 
		fields = '__all__'
