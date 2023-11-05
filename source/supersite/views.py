from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Video
from .forms import VideoUploadForm, UserRegistrationForm


@login_required
def start(request):
    template_name = 'base.html'
    context = {}
    return render(request, template_name, context)


@login_required
def upload_video(request):
    if request.method == 'GET':
        form = VideoUploadForm()
    elif request.method == 'POST':
        form = VideoUploadForm(data=request.POST, files=request.FILES)
        print(request.POST, request.FILES, form)
        if form.is_valid():
            form.save()
            return redirect('start_page')
    template_name = 'upload_video.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)


def register(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
    elif request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
    template_name = 'registration/registration.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)
