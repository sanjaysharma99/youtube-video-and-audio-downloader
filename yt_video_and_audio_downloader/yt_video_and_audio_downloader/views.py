from django.shortcuts import render 
from django.http import FileResponse 
from .yttool import download_audio_and_video 
from django.views.decorators.http import require_POST 

def home(request):
    return render(request,'home.html')

@require_POST 
def convert(request):
    if request.method=='POST':
        video_url=request.POST.get('video_url')
        video_file_path,audio_file_path=download_audio_and_video(video_url)

        context={'video_file':video_file_path,'audio_file':audio_file_path}
        return render(request,'download.html',context)
    
@require_POST 
def download(request):
    if request.method=='POST':
        file_path=request.POST.get('file_path')
        return FileResponse(open(file_path,'rb'),as_attachment=True)
    
