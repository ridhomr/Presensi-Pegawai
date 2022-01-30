from django.shortcuts import render
from  .forms import UploadForm 
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def upload(request):
	form = UploadForm(request.POST or None, request.FILES or None)
	if request.is_ajax():
		if form.is_valid():
			form.save()
			return JsonResponse({'message':"hell yeah"})
	context = {
		'form': form,
	}
	return render(request, 'uploads/upload_ajax.html', context)