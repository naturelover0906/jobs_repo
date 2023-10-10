from django.shortcuts import render
from testapp.models import HydJobs
from testapp.models import PuneJobs
from testapp.models import BngJobs

# Create your views here.
def jobs_view(request):
    return render(request,'testapp/index.html')

def hydjobinfo(request):
    jobtitle='HydJobs'
    cap_msg='Companies Info of HYDERABAD:'
    head_msg='Hyderabad Jobs Informations'
    type='hydjobs'
    job_list=HydJobs.objects.all()
    my_dict={'job_list':job_list,'jobtitle':jobtitle,'head_msg':head_msg,'cap_msg':cap_msg,'type':type}
    return render(request,'testapp/jobs.html',my_dict)

def punejobinfo(request):
    jobtitle='PuneJobs'
    head_msg='Pune Jobs Informations'
    cap_msg='Companies Info Of PUNE:'
    type='punejobs'
    job_list=PuneJobs.objects.all()
    my_dict={'job_list':job_list,'jobtitle':jobtitle,'head_msg':head_msg,'cap_msg':cap_msg,'type':type}
    return render(request,'testapp/jobs.html',my_dict)

def banglorejobinfo(request):
    jobtitle='BangloreJobs'
    head_msg='Banglore Jobs Informations'
    cap_msg='Companies Info Of BANGLORE:'
    type='bngjobs'
    job_list=BngJobs.objects.all()
    my_dict={'job_list':job_list,'jobtitle':jobtitle,'head_msg':head_msg,'cap_msg':cap_msg,'type':type}
    return render(request,'testapp/jobs.html',my_dict)
