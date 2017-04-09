#!/usr/bin/env python
#coding:utf-8
#__author__="ybh"
from django.forms import forms
class FileUploadForm(forms.Form):
    my_file=forms.FileField()