from django.contrib import admin
from testapp.models import HydJobs
from testapp.models import PuneJobs
from testapp.models import BngJobs
# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligible','address','email','phone']
admin.site.register(HydJobs,HydJobsAdmin)

class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligible','address','email','phone']
admin.site.register(PuneJobs,PuneJobsAdmin)

class BngJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','eligible','address','email','phone']
admin.site.register(BngJobs,BngJobsAdmin)