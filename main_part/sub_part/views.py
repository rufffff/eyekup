from django.shortcuts import redirect, render
from django.contrib import messages
from . models import Message,Registration,job_category,skill,joblocation,company,Job,jobapplication,candidate_database,job_onboard,Interview_schedule
import easygui
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def addinterviewschedule(request):
    if request.method=='POST':
        reg_dis=Interview_schedule(Candidate=request.POST['Candidate'],
                        Employee=request.POST['Employee'],
                        date=request.POST['date'],
                        time=request.POST['time'],
                        ) 
        reg_dis.save()
        easygui.msgbox("added successfully!...")
        return redirect(interviewschedule)
    return render(request,'addinterviewschedule.html')

def blank(request):
    return render(request,'blank.html') 

def candidatedatabase(request):
    var1=candidate_database.objects.all()
    return render(request,'candidatedatabase.html',{'var1':var1})

def companies(request):
    var1=company.objects.all()
    return render(request,'companies.html',{'var1':var1})

def contact(request):
    return render(request,'contact.html')

def createnewjobs(request):
    if request.method=='POST':
        reg_dis=Job(company_name=request.POST['company_name'],
                job_title=request.POST['job_title'],
                job_discription=request.POST['job_discription'],
                job_requirement=request.POST['job_requirement'],
                job_location=request.POST['job_location'],
                job_category=request.POST['job_category'],
                skills=request.POST['skills'],
                total_positions=request.POST['total_positions'],
                start_date=request.POST['start_date'],
                end_date=request.POST['end_date'],
                meta_title=request.POST['meta_title'],
                )
        reg_dis.save()
        easygui.msgbox('added successfully!...')
        return redirect(jobs)
    return render(request,'createnewjobs.html') 

def newcandidatedatabase(request):
    if request.method=='POST':
        reg_dis=candidate_database(Applicant_Name=request.POST['Applicant_Name'],
                 jobs=request.POST['jobs'],
                 Job_locations=request.POST['Job_locations'],
                 )
        reg_dis.save()
        easygui.msgbox('added successfully!...')
        return redirect(candidatedatabase)
    return render(request,'newcandidatedatabase.html') 

def createnewjobonboard(request):
    if request.method=='POST':
        reg_dis=job_onboard(Applicant_Name=request.POST['Applicant_Name'],
                jobs=request.POST['jobs'],
                Job_locations=request.POST['Job_locations'],
                joining_date=request.POST['joining_date'],
                accept_last_date=request.POST['accept_last_date'],
                status=request.POST['status'],
                )
        reg_dis.save()
        easygui.msgbox('added successfully!...')
        return redirect(Jobonboard)
    return render(request,'createnewjobonboard.html') 

def dashboard(request):
    return render(request,'dashboard.html')

def interviewschedule(request):
    return render(request,'interviewschedule.html')

def jobapplications(request):
    return render(request,'jobapplications.html')

def jobcategories(request):
    var1=job_category.objects.all()
    return render(request,'jobcategories.html',{'var1':var1})

def Joblocations(request):
    var1=joblocation.objects.all()
    return render(request,'Joblocations.html',{'var1':var1}) 

def Jobonboard(request):
    var1=job_onboard.objects.all()
    return render(request,'Jobonboard.html',{'var1':var1})

def jobs(request):
    var1=Job.objects.all()
    return render(request,'jobs.html',{'var1':var1})

def newcompanies(request):
    if request.method=='POST':
        reg_dis=company(companyname=request.POST['companyname'],
                    email=request.POST['email'],
                    phone=request.POST['phone'],
                    website=request.POST['website'],
                    address=request.POST['address'],
                    status=request.POST['status'],
                    )
        if len(request.FILES) !=0:
            reg_dis.logo=request.FILES['logo']
        reg_dis.save()
        easygui.msgbox("added successfully!...") 
        return redirect(companies)
    return render(request,'newcompanies.html')

def newjobcategories(request):
    if request.method=='POST':
        reg_dis=job_category(jobname=request.POST['jobname'],
                     ) 
        reg_dis.save()
        easygui.msgbox("added successfully!...")
        return redirect(jobcategories)
    return render(request,'newjobcategories.html') 

def newjoblocations(request):
    if request.method=='POST':
        reg_dis=joblocation(joblocationname=request.POST['joblocationname'],
                            country=request.POST['country']
                            ) 
        reg_dis.save()
        easygui.msgbox("added successfully!...")
        return redirect(Joblocations)
    return render(request,'newjoblocations.html')

def newskills(request):
    if request.method=='POST':
        reg_dis=skill(jobcategory=request.POST['jobcategory'],
                           skillname=request.POST['skillname']
                           ) 
        reg_dis.save()
        easygui.msgbox("added successfully!...")
        return redirect(skills)
    return render(request,'newskills.html')

def profile(request):
    return render(request,'profile.html')

def report(request):
    return render(request,'report.html')

def services(request):
    return render(request,'services.html') 

def skills(request):
    var1=skill.objects.all()
    return render(request,'skills.html',{'var1':var1})

def todos(request):
    return render(request,'todos.html')                   

def timeline(request):
    return render(request,'timeline.html')

def register(request):
    return render(request,'register.html')



def contact_us(request):
    if request.method=='POST':
        reg_dis=Message(name=request.POST['name'],
                     email=request.POST['email'],
                     subject=request.POST['subject'],
                     message=request.POST['message'],
                     ) 
        reg_dis.save()
        easygui.msgbox("message sent successfully!...")
        return redirect(index)
    return render(request,'index.html')


def Register(request):
    if request.method=='POST':
        if Registration.objects.filter(Username=request.POST['Username']).exists():
            context={'msg':'Username is already exist'}
            return render(request,'register.html',context)
        elif Registration.objects.filter(email=request.POST['email']).exists():
            context1={'msg1':'email is already exist'}
            return render(request,'register.html',context1)
        elif request.method=='POST':
            reg_dis=Registration(First_Name=request.POST['First_Name'],
                    Last_Name=request.POST['Last_Name'],
                    Username=request.POST['Username'],
                    phone_number=request.POST['phone_number'],
                    email=request.POST['email'],
                    password=request.POST['password'],
                    ) 
            reg_dis.save()
            easygui.msgbox("you are registered successfully!...")
            return redirect(login)
    return render(request,'login.html')


def login(request):
    if request.method=='POST':
        if Registration.objects.filter(Username=request.POST['Username'],password=request.POST['password']).exists():
            ex1=Registration.objects.get(Username=request.POST['Username'],password=request.POST['password'])
            easygui.msgbox("successfully logged in!...")
            return render(request,'dashboard.html',{'ex1':ex1})
        else:
            easygui.msgbox("invalid Username or password!...")
            return render(request,'login.html')
    return render(request,'login.html')


def logout(request):
    log(request)
    easygui.msgbox("logged out")
    return render(request,'login.html')


def jobcategoriesedit(request,id):
    var2=job_category.objects.get(id=id)
    return render(request,'jobcategoriesedit.html',{'var2':var2})
     
def jobcategoriesupdate(request,id):
    var2=job_category(id=id,jobname=request.POST['jobname'])
    var2.save()
    easygui.msgbox("your data has been updated successfully!...")
    return redirect(jobcategories)


def jobcategoriesdelete(request,id):
    var2=job_category.objects.get(id=id)
    var2.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(jobcategories)


def skillsedit(request,id):
    var3=skill.objects.get(id=id)
    return render(request,'skillsedit.html',{'var3':var3})
     
def skillsupdate(request,id):
    var3=skill(id=id,skillname=request.POST['skillname'],
                    jobcategory=request.POST['jobcategory'])
    var3.save()
    easygui.msgbox("your data has been updated successfully!...")
    return redirect(skills)

def skillsdelete(request,id):
    var3=skill.objects.get(id=id)
    var3.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(skills)

def joblocationsedit(request,id):
    var4=joblocation.objects.get(id=id)
    return render(request,'joblocationsedit.html',{'var4':var4})
     
def joblocationsupdate(request,id):
    var4=joblocation(id=id,joblocationname=request.POST['joblocationname'],
                    country=request.POST['country'])
    var4.save()
    easygui.msgbox("your data has been updated successfully!...")
    return redirect(Joblocations)

def joblocationsdelete(request,id):
    var4=joblocation.objects.get(id=id)
    var4.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(Joblocations)

def companiesedit(request,id):
    var5=company.objects.get(id=id)
    return render(request,'companiesedit.html',{'var5':var5})
     
def companiesupdate(request,id):
    var5=company(id=id,logo=request.FILES['logo'],
                companyname=request.POST['companyname'],
                email=request.POST['email'],
                status=request.POST['status'])
    var5.save()
    easygui.msgbox("your data has been updated successfully!...")
    return redirect(companies)

def companiesdelete(request,id):
    var5=company.objects.get(id=id)
    var5.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(companies)

def jobsedit(request,id):
    var6=Job.objects.get(id=id)
    return render(request,'jobsedit.html',{'var6':var6})
     
def jobsupdate(request,id):
    var6=Job(id=id,company_name=request.POST['company_name'],
                job_title=request.POST['job_title'],
                job_discription=request.POST['job_discription'],
                job_requirement=request.POST['job_requirement'],
                job_location=request.POST['job_location'],
                job_category=request.POST['job_category'],
                skills=request.POST['skills'],
                total_positions=request.POST['total_positions'],
                start_date=request.POST['start_date'],
                end_date=request.POST['end_date'],
                meta_title=request.POST['meta_title'],
                )
    var6.save()
    easygui.msgbox("your data has been updated successfully!...")
    return redirect(jobs)

def jobsdelete(request,id):
    var6=Job.objects.get(id=id)
    var6.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(jobs)

def createnewjobapplication(request):
    if request.method=='POST':
        reg_dis=jobapplication(job=request.POST['job'],
                           Name=request.POST['Name'],
                           email=request.POST['email'],
                           phone=request.POST['phone']
                           ) 
        reg_dis.save()
        easygui.msgbox("added successfully!...")
        return redirect(jobapplications)
    return render(request,'createnewjobapplication.html')

def candidatedatabaseedit(request,id):
    var7=candidate_database.objects.get(id=id)
    return render(request,'candidatedatabaseedit.html',{'var7':var7})
     
def candidatedatabaseupdate(request,id):
    var7=candidate_database(id=id,Applicant_Name=request.POST['Applicant_Name'],
                            jobs=request.POST['jobs'],
                            Job_locations=request.POST['Job_locations']
                            )
    var7.save()
    easygui.msgbox("your data has been updated successfully!...")
    return redirect(candidatedatabase)

def candidatedatabasedelete(request,id):
    var7=candidate_database.objects.get(id=id)
    var7.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(candidatedatabase)

def jobonboardedit(request,id):
    var8=job_onboard.objects.get(id=id)
    return render(request,'jobonboardedit.html',{'var8':var8})
     
def jobonboardupdate(request,id):
    var8=job_onboard(id=id,Applicant_Name=request.POST['Applicant_Name'],
                            jobs=request.POST['jobs'],
                            Job_locations=request.POST['Job_locations'],
                            joining_date=request.POST['joining_date'],
                            accept_last_date=request.POST['accept_last_date'],
                            status=request.POST['status']
                            )
    var8.save()
    easygui.msgbox("your data has been updated successfully!...")
    return redirect(Jobonboard)

def jobonboarddelete(request,id):
    var8=job_onboard.objects.get(id=id)
    var8.delete()
    easygui.msgbox("your data has been deleted successfully")
    return redirect(Jobonboard)





