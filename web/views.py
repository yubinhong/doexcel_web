from django.shortcuts import render,HttpResponse,redirect
from web.forms import FileUploadForm
from backend import main,download
import time,os
# Create your views here.


def index(request):
    return render(request,'index.html')

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
    path='yuming'
    if request.method == 'POST':
        files=request.FILES.getlist('my_files')
        dir=return_files_dir(files,path)
        downloadfile=main.yuming(dir)
        print(downloadfile)
        #response=download.download(downloadfile)
        #return redirect('http://doexcel.miguan.com%s' % (downloadfile))
        return redirect('%s' % (downloadfile))

    return render(request, 'yuming.html')

def dianshang(request):
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
    path='dianshang'
    if request.method == 'POST':
        files=request.FILES.getlist('my_files')
        dir=return_files_dir(files,path)
        downloadfile=main.dianshang(dir)
        print(downloadfile)
        #response=download.download(downloadfile)
        #return redirect('http://doexcel.miguan.com%s' % (downloadfile))
        return redirect('%s' % (downloadfile))

    return render(request, 'dianshang.html')

def daohang(request):
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
    path='daohang'
    if request.method == 'POST':
        files=request.FILES.getlist('my_files')
        dir=return_files_dir(files,path)
        downloadfile=main.daohang(dir)
        print(downloadfile)
        #response=download.download(downloadfile)
        #return redirect('http://doexcel.miguan.com%s' % (downloadfile))
        return redirect('%s' % (downloadfile))

    return render(request, 'daohang.html')

def ruanjian(request):
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
    path='ruanjian'
    if request.method == 'POST':
        files=request.FILES.getlist('my_files')
        dir=return_files_dir(files,path)
        downloadfile=main.ruanjian(dir)
        print(downloadfile)
        #response=download.download(downloadfile)
        #return redirect('http://doexcel.miguan.com%s' % (downloadfile))
        return redirect('%s' % (downloadfile))

    return render(request, 'ruanjian.html')


def return_files_dir(files,path):
    basedir='/tmp'
    basedir2=os.path.join(basedir,path)
    ctime=time.strftime("%Y%m%d%H%M%S", time.localtime())
    dir=os.path.join(basedir2,ctime)
    os.makedirs(dir)

    for f in files:
        with open(dir+"/"+f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    return dir
