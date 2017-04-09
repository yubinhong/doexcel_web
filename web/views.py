from django.shortcuts import render,HttpResponse
from web.forms import FileUploadForm
from backend import main,download
import time,os
# Create your views here.

def yuming(request):
    """
      文件接收 view
      :param request: 请求
      :return:
      """
    """
    文件接收 view
    :param request: 请求
    :return:
    """
    if request.method == 'POST':
        files=request.FILES.getlist('my_files')
        dir=return_files_dir(files)
        downloadfile=main.yuming(dir)
        response=download.download(downloadfile)
        return response

    return render(request, 'result.html')


def return_files_dir(files):
    basedir='/tmp'
    ctime=time.strftime("%Y%m%d%H%M%S", time.localtime())
    dir=os.path.join(basedir,ctime)
    os.makedirs(dir)

    for f in files:
        with open(dir+"/"+f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    return dir