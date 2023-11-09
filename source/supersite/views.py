from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators import gzip
from django.http import StreamingHttpResponse

from .models import Video, Camera
from .forms import VideoUploadForm, CameraAddForm, UserRegistrationForm

from source.services import set_auth_for_camera
from .stream import VideoCamera, gen


@login_required
def start(request):
    videos = Video.objects.filter(author=request.user)
    cameras = Camera.objects.filter(author=request.user)
    template_name = 'base.html'
    context = {
        'videos': videos,
        'cameras': cameras
    }
    return render(request, template_name, context)


@login_required
def upload_video(request):
    if request.method == 'GET':
        form = VideoUploadForm()
    elif request.method == 'POST':
        form = VideoUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_video = form.save(commit=False)
            new_video.author = request.user
            form.save()
            return redirect('start_page')
    template_name = 'form.html'
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


@login_required
def result(request, camera_id):
    template_name = 'result.html'
    context = {
        'camera_id': camera_id
    }
    return render(request, template_name, context)


@login_required
@gzip.gzip_page
def stream(request, camera_id=None):
    camera = Camera.objects.get(id=camera_id)
    auth_data = {
        'url': camera.camera_url,
        'username': camera.username,
        'password': camera.password
    }
    url = set_auth_for_camera(data=auth_data)
    cam = VideoCamera(url=url)
    return StreamingHttpResponse(gen(cam), content_type='multipart/x-mixed-replace;boundary=frame')


@login_required
def add_camera(request):
    if request.method == 'GET':
        form = CameraAddForm()
    elif request.method == 'POST':
        form = CameraAddForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_video = form.save(commit=False)
            new_video.author = request.user
            form.save()
            return redirect('start_page')
    template_name = 'form.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)
