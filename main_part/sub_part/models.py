from django.db import models

# Create your models here.

class Message(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
   
    def __str__(self):
        return self.email


class Registration(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Username=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=15)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.email

class job_category(models.Model):
    jobname=models.CharField(max_length=100)
    
    def __str__(self):
        return self.jobname

class skill(models.Model):
    skillname=models.CharField(max_length=100)
    jobcategory=models.CharField(max_length=100)
    
    def __str__(self):
        return self.skillname

class joblocation(models.Model):
    joblocationname=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    
    def __str__(self):
        return self.joblocationname


class company(models.Model):
    companyname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    website=models.URLField(max_length=100)
    logo=models.ImageField(upload_to='media/img',null=True)
    address=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
   
    def __str__(self):
        return self.companyname

class Job(models.Model):
    company_name=models.CharField(max_length=100,default=None)
    job_title=models.CharField(max_length=100,default=None)
    job_discription=models.CharField(max_length=100,default=None)
    job_requirement=models.CharField(max_length=100,default=None)
    job_location=models.CharField(max_length=100,default=None)
    job_category=models.CharField(max_length=100,default=None)
    skills=models.CharField(max_length=100,default=None)
    total_positions=models.CharField(max_length=100,default=None)
    start_date=models.DateField(max_length=100,default=None)
    end_date=models.DateField(max_length=100,default=None)
    skills=models.CharField(max_length=100,default=None)
    meta_title=models.CharField(max_length=100,default=None)

    def __str__(self):
        return self.job_title
   
class jobapplication(models.Model):
    job=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name

class candidate_database(models.Model):
    Applicant_Name=models.CharField(max_length=100)
    jobs=models.CharField(max_length=100)
    Job_locations=models.CharField(max_length=100)
   
    def __str__(self):
        return self.Applicant_Name

class job_onboard(models.Model):
    Applicant_Name=models.CharField(max_length=100)
    jobs=models.CharField(max_length=100)
    Job_locations=models.CharField(max_length=100)
    joining_date=models.DateField(max_length=100)
    accept_last_date=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
   
    def __str__(self):
        return self.Applicant_Name

class Interview_schedule(models.Model):
    Candidate=models.CharField(max_length=100)
    Employee=models.CharField(max_length=100)
    date=models.DateField(max_length=100)
    time=models.TimeField(max_length=100)
    
    def __str__(self):
        return self.Candidate


