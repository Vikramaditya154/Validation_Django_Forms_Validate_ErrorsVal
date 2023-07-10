from django.shortcuts import render

# Create your views here.
from app.forms import *

from django.http import HttpResponse

def student_form(request):
    SFD=StudentForm()
    if request.method=='POST':
        SF=StudentForm(request.POST)
        if SF.is_valid():
            return HttpResponse('Data is submited')
        else:
            return HttpResponse('data is not valid')
    return render(request,'student_form.html',{'SFD':SFD})