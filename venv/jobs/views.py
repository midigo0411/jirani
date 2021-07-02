from django.shortcuts import render

from django.http import HttpResponse

from .models import jobs


def index(request):
    jobs = jobs.objects
    return render(request, 'jobs/index.html',{'jobs':jobs})

def detail(request,jobs_id):
    print(jobs_id),
    return render(request, 'jobs/index.html'),  

 



# Create your views here.
