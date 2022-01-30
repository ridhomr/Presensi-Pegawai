from django import forms
from staf_pegawai.models import Feedback

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = '__all__'
		labels = {
			'masukkan':'Masukkan Dan Saran',
		}