import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','modelproject_manojob5.settings')
import django
django.setup()

from testapp.models import HydJobs
from testapp.models import PuneJobs
from testapp.models import BngJobs
from faker import Faker
from random import *

fake=Faker()
def phonenumbergen():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)

def populate(n):
    title_list=['Marketing Coordinator','Medical Assistant','Web Designer','President of Sales','Project Manager','Librarian','Project Manager','Account Executive','Software Engineer','Associate Manager','Team Leader']
    eligible_list=['M.Tech','B.Tech','MCA','BCA','Phd','MBA','BBus','Msc','MBus','McompSc']
    for k in range(3):
        for i in range(n):
            fdate=fake.date()
            fcompany=fake.company()
            ftitle=fake.random_element(title_list)
            feligible=fake.random_element(eligible_list)
            faddress=fake.address()
            femail=fake.company_email()
            fphone=phonenumbergen()
            if k==0:
                HydJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligible=feligible,address=faddress,email=femail,phone=fphone)
            if k==1:
                PuneJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligible=feligible,address=faddress,email=femail,phone=fphone)
            if k==2:
                BngJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligible=feligible,address=faddress,email=femail,phone=fphone)


n = int(input('Enter number of records you want: '))
populate(n)
print(f'{n} Records Inserted in Database Successfully!!')