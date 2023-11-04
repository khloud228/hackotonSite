from django.shortcuts import render, redirect

from .models import Video
from .forms import VideoUploadForm


def start(request):
    template_name = 'base.html'
    context = {}
    return render(request, template_name, context)



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
