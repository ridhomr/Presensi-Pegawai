from django import forms 
from .models import Log, Absensi
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from django.core.exceptions import ValidationError

class PresensiForm(forms.ModelForm):
	class Meta:
		model = Absensi
		fields = '__all__'
		labels = {
			'status':'Status',
			'keterangan':'Masukkan Keterangan'
		}

