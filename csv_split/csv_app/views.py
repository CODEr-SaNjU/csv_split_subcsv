from django.shortcuts import render ,redirect 
from django.http import HttpResponse, Http404
import re
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage
from .models import Documents
import csv 
# from .forms import DocumentForm
# from selenium import webdriver
from django.http import FileResponse
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper
import random



def csv_files(request):
    if request.method == 'POST' and request.FILES['files']:
        myfile = request.FILES['files']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = os.path.join(settings.BASE_DIR+fs.url(filename))
        if os.path.exists(uploaded_file_url)==True:
            with open(uploaded_file_url,'r') as csvfile:
                csvfile = csvfile.readlines()
                basefilename, file_extension= os.path.splitext(filename)
                # print("radhe_radhe ",basefilename,file_extension)
                # chars= 'Download'
                # randomstr= ''.join((random.choice(chars)) for x in range(10))
                new_file_name = '{randomstring}{ext}'.format(randomstring= "Download", ext= file_extension)
                # file_path = os.path.join(settings.MEDIA_ROOT, new_file_name)
                # print(new_file_name)
                new_file_name_lines = open(new_file_name,'w')
                new_file_name_lines.writelines("hello world")
                # print(new_file_name)
                if os.path.exists(new_file_name):
                    print("FOUND File 'tempCSV.csv'")
                    with open(new_file_name, 'w') as f:
                        for input in csvfile:
                            f.writelines(input)
                            # print(f)
                    with open(new_file_name, 'rb') as fh:
                        response = HttpResponse(
                            fh.read(), content_type="text/csv;charset=utf-8;")
                        response['Content-Disposition'] = 'attachment; filename=' + new_file_name
                        return response
                else:
                    print("File 'tempDownloadCSV.csv' does not exist")
          
            return render(request, 'html_files/Home.htm',)
        else:
            return HttpResponse("please remove space from filename ya add _ in filename")

    return render(request, 'html_files/Home.htm')








#  for csvline in csvfile:
#                     if csvline == '\n':
#                         continue
#                     csvline = re.sub(',,+','',csvline)
#                     csvlinelist = csvline.split(',')
#                     if len(csvlinelist) == 1:
#                         print("len == 1")
#                         files_name=csvline.strip('\n')+'.csv'
#                         print("filename == ",files_name)
#                         uploaded_file_url_1 = os.path.join(settings.MEDIA_ROOT,files_name)
#                         subcsvfile=open(uploaded_file_url_1,'w',)
#                         continue
#                     new_file_csv = subcsvfile.write(csvline)
#                     print("last file data",new_file_csv)
#                 file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file_url_1)
#                 if os.path.exists(file_path):
#                     # subcsvfile_1 = open(file_path, 'w')
#                     with open(file_path, 'w') as fh:
#                         response = HttpResponse(new_file_csv, content_type="text/csv;charset=utf-8;")
#                         response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#                         return response
#                 raise Http404
