from django.shortcuts import render
from .models import Student
from django.contrib import messages
from django.db.models import Q
from tablib import Dataset

# Create your views here.

def upload(request):
    if request.method == 'POST':
        dataset = Dataset()
        new_student = request.FILES['myfile']

        if not new_student.name.endswith('xlsx'):
            messages.info(request, 'File must be in xlsx format')
            return render(request, 'upload.html')

        imported_data = dataset.load(new_student.read(), format='xlsx')
        for data in imported_data:
            value = Student(
                ien = data[0],
                name = data[1],
                branch = data[2],
                attendence = data[3]
            )
            value.save()

    return render(request, 'upload.html')


def index(request):

    if request.GET.get('search_text') != None:
        q = request.GET.get('search_text')
    else:
        q = ''

    students = Student.objects.filter(ien__icontains=q)
    
    # if request.method == 'POST':
    #     search_text = request.POST['search_text']
    #     students = Student.objects.filter(ien__icontains=search_text)
    
    return render(request, 'index.html', {'students': students})