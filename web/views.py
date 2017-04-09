from django.shortcuts import render,HttpResponse
from web.forms import FileUploadForm
from backend import main

# Create your views here.
'''
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
        my_form = FileUploadForm(request.POST, request.FILES)
        if my_form.is_valid():
            f = my_form.cleaned_data['my_file']
            handle_uploaded_file(f)
        return HttpResponse('Upload Success')
    else:
        my_form = FileUploadForm()
    return render(request, 'yuming.html', {'form': my_form})



def handle_uploaded_file(f):
    with open("d:\\"+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

'''



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
        handle_uploaded_files(files)
        return HttpResponse('Upload Success')

    return render(request, 'result.html')


def handle_uploaded_files(files):
    for f in files:
        with open("d:\\"+f.name, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
