from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date

def index(request):
    return render(request, 'app/index.html')



def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error="yes"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'app/admin_login.html', d)

def user_login(request):
    error=""
    if request.method == 'POST':
       u = request.POST['uname'];
       p = request.POST['pwd'];
       user = authenticate(username=u, password=p)
       if user:
            try:
               user1 = SUser.objects.get(user=user)
               if user1.type == "seeker":
                   login(request, user)
                   error="no"
               else:
                   error="yes"
            except:
               error="yes"
       else:
            error="yes"
    d = {'error': error}
    return render(request, 'app/user_login.html', d)

def recruiter_login(request):
    error=""
    if request.method == 'POST':
       u = request.POST['uname'];
       p = request.POST['pwd'];
       user = authenticate(username=u, password=p)
       if user:
            try:
               user1 = Recruiter.objects.get(user=user)
               if user1.type == "recruiter" and user1.status!="pending":
                   login(request, user)
                   error="no"
               elif user1.type == "recruiter" and user1.status == "pending":
                   login(request, user)
                   error="not"
            except:
               error="yes"
       else:
            error="yes"
    d = {'error': error}
    return render(request, 'app/recruiter_login.html', d)


def recruiter_signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']
        company = request.POST['company']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            Recruiter.objects.create(user=user, mobile=con, image=i, gender=gen, company=company, type="recruiter", status="pending")
            error="no"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'app/recruiter_signup.html', d)

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request, 'app/user_home.html')

def Logout(request):
    logout(request)
    return redirect('index')

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'app/admin_home.html')

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    return render(request, 'app/recruiter_home.html')


def user_signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            SUser.objects.create(user=user, mobile=con, image=i, gender=gen, type="seeker")
            error="no"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'app/user_signup.html',d)


def view_users(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = SUser.objects.all()
    d = {'data': data}
    return render(request, 'app/view_users.html', d)


def delete_user(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    seeker = User.objects.get(id=pid)
    seeker.delete()
    return redirect('view_users')

def delete_recruiter(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiter = User.objects.get(id=pid)
    recruiter.delete()
    return redirect('recruiter_all')

def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='pending')
    d = {'data': data}
    return render(request, 'app/recruiter_pending.html', d)

def change_status(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    recruiter = Recruiter.objects.get(id=pid)
    
    if request.method=='POST':
        s = request.POST['status']
        recruiter.status = s
        try:
            recruiter.save()
            error="no"
        except:
            error="yes"
        
    d = {'recruiter': recruiter, 'error':error}
    return render(request, 'app/change_status.html', d)

def change_passwordadmin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""

    if request.method=='POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="no"
        except:
            error="yes"
        
    d = {'error':error}
    return render(request, 'app/change_passwordadmin.html', d)


def change_passworduser(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error=""

    if request.method=='POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="no"
        except:
            error="yes"
        
    d = {'error':error}
    return render(request, 'app/change_passworduser.html', d)

def change_passwordrecruiter(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=""

    if request.method=='POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error="no"
            else:
                error="no"
        except:
            error="yes"
        
    d = {'error':error}
    return render(request, 'app/change_passwordrecruiter.html', d)


def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='Accept')
    d = {'data': data}
    return render(request, 'app/recruiter_accepted.html', d)

def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status='Reject')
    d = {'data': data}
    return render(request, 'app/recruiter_rejected.html', d)

def recruiter_all(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.all()
    d = {'data': data}
    return render(request, 'app/recruiter_all.html', d)


def add_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=""
    if request.method == 'POST':
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        l = request.FILES['logo']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['description']
        user = request.user
        recruiter = Recruiter.objects.get(user=user)
        try:
            Job.objects.create(recruiter=recruiter, start_date=sd, end_date=ed, title=jt, salary=sal, image=l, description=des, experience=exp, location=loc, skills=skills, creationdate=date.today())
            error="no"
        except:
            error="yes"
    d = {'error': error}
    return render(request, 'app/add_job.html', d)


def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    job = Job.objects.filter(recruiter=recruiter)
    d = {'job': job}
    return render(request, 'app/job_list.html', d)


def edit_jobdetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error=""
    job = Job.objects.get(id=pid)
    if request.method == 'POST':
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['description']
        
        job.title = jt
        job.salary = sal
        job.experience = exp
        job.location = loc
        job.skills = skills
        job.description = des
        
                
        try:
            job.save()
            error="no"
        except:
            error="yes"
        if sd:
            try: 
                job.start_date = sd
                job.save()
            except:
                pass
        else:
            pass
        
        if ed:
            try: 
                job.end_date = sd
                job.save()
            except:
                pass
        else:
            pass
        
        
        
        
    d = {'error': error, 'job': job}
    return render(request, 'app/edit_jobdetail.html', d)









from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(user=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             return redirect('user_home')
#         else:
#             return render(request, 'app/change_password.html', {'form': form, 'error': 'yes'})
#     else:
#         form = PasswordChangeForm(user=request.user)
#     return render(request, 'app/change_password.html', {'form': form})


