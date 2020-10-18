from django.shortcuts import render ,redirect 
from django.http import HttpResponse, Http404
import re
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage
from .models import Documents
import csv 
from .forms import DocumentForm
from django.http import FileResponse
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper
import random

def csv_files(request):
    if request.method == 'POST' and request.FILES['files']:
        myfile = request.FILES['files']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print(filename)
        uploaded_file_url = os.path.join(settings.BASE_DIR+fs.url(filename))
        print(uploaded_file_url)
        if os.path.exists(uploaded_file_url)==True:
            with open(uploaded_file_url,'r') as csvfile:
                csvfile = csvfile.readlines()
                for csvline in csvfile:
                    if csvline == '\n':
                        continue
                    csvline = re.sub(',,+','',csvline)
                    csvlinelist = csvline.split(',')
                    if len(csvlinelist) == 1:
                        files_name=csvline.strip('\n')+'.csv'
                        uploaded_file_url_1 = os.path.join(settings.MEDIA_ROOT,files_name)
                        subcsvfile=open(uploaded_file_url_1,'w',)
                        continue
                    new_file_csv = subcsvfile.write(csvline)
            return render(request, 'html_files/Home.htm',)
        else:
            return HttpResponse("please remove space from filename ya add _ in filename")

    return render(request, 'html_files/Home.htm')






