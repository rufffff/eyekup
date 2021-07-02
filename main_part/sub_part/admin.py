from django.contrib import admin
from . models import Message,Registration,job_category,skill,joblocation,company,Job,jobapplication,candidate_database,job_onboard,Interview_schedule

# Register your models here.
admin.site.register(Message)
admin.site.register(Registration)
admin.site.register(job_category)
admin.site.register(skill)
admin.site.register(joblocation)
admin.site.register(company)
admin.site.register(Job)
admin.site.register(jobapplication)
admin.site.register(candidate_database)
admin.site.register(job_onboard)
admin.site.register(Interview_schedule)