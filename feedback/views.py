from django.shortcuts import render, redirect
from staf_pegawai.models import Feedback
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import FeedbackForm

# Create your views here.
def feedback_list(request):
	context = {'daftar_feedback': Feedback.objects.all()}
	return render(request, "dashboard/feedback_list.html", context)

def feedback_form(request, id=0):
	if request.method == "POST":
		if id == 0:
			form = FeedbackForm(request.POST)
		else:
			feed = Feedback.objects.get(pk=id)
			form = FeedbackForm(request.POST, instance=feed)
		form.save()
		return redirect('/dashboard/feedback/list')

	else:
		if id == 0:
			form = FeedbackForm()
		else:
			feed = Feedback.objects.get(pk=id)
			form = FeedbackForm(instance=feed)
		return render(request, "dashboard/feedback_form.html", {'form': form})

def feedback_delete(request, id):
	feed = Feedback.objects.get(pk=id)
	feed.delete()
	return redirect('/dashboard/feedback/list')