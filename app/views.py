from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.models import Jobs, Datas, ApplyJob
from rest_framework.filters import SearchFilter
from django.contrib import messages

@login_required(login_url='signup')
def HomePage(request):
    

    job=Jobs.objects.all()

    context={
                'job':job, 
            }

    return render (request,'home.html',context)

@login_required(login_url='signup1')
def HomePage1(request):
    
    job=Jobs.objects.all()
    context1={
        'job':job,
    }
    return render (request,'home1.html',context1)

@login_required(login_url='signup1')
def Profile1(request):
    try:
        data=Datas.objects.get(user=request.user)
    except Exception as e:
        data=None
        print('Exception:', e)

    context1={
        'data':data,
    }

    return render (request,'profile1.html', context1)

@login_required(login_url='signup')
def Profile(request):
    try:
        data=Datas.objects.get(user=request.user)
    except Exception as e:
        data=None
        print('Exception:', e)

    context1={
        'data':data,
    }

    return render (request,'profile.html', context1)

def Pedit(request):
    context = {}
    check = Datas.objects.filter(user__id=request.user.id)
    if len(check)>0:
        data = Datas.objects.get(user__id=request.user.id)
        context["data"]=data    
    if request.method=="POST":
        
        age = request.POST.get("age")
        qualification = request.POST.get("qualification")
        exp = request.POST.get("exp")
        skills = request.POST.get("skills")
        phone=request.POST.get("phone")       
       
        data.age = age
        data.qualification = qualification
        data.exp = exp
        data.skills = skills
        data.phone = phone
        data.save()

        context["status"] = "Changes Saved Successfully"
        messages.success(request, "Changes Saved Successfully ! ")
    return render(request,"pedit.html",context)
        
def Pedit1(request):
    context = {}
    check = Datas.objects.filter(user__id=request.user.id)
    if len(check)>0:
        data = Datas.objects.get(user__id=request.user.id)
        context["data"]=data    
    if request.method=="POST":
        
        age = request.POST.get("age")
        qualification = request.POST.get("qualification")
        exp = request.POST.get("exp")
        skills = request.POST.get("skills")
        phone=request.POST.get("phone")       
       
        data.age = age
        data.qualification = qualification
        data.exp = exp
        data.skills = skills
        data.phone = phone
        data.save()

        context["status"] = "Changes Saved Successfully"
        messages.success(request, "Changes Saved Successfully ! ")
    return render(request,"pedit1.html",context)

def SignupPage(request):
    if request.method=='POST':
         username=request.POST.get('username')
         email=request.POST.get('email')
         password=request.POST.get('password')
         password1=request.POST.get('password1')

         if password!=password1:
            messages.success(request, "Password and Confirm Password are not same ! ")
         else:
            my_user=User.objects.create_user(username,email,password)
            my_user.save()
            return redirect('login')
    return render(request, 'index.html')

def SignupPage1(request):
    if request.method=='POST':
         username2=request.POST.get('username2')
         email2=request.POST.get('email2')
         password2=request.POST.get('password2')
         password12=request.POST.get('password12')

         if password2!=password12:
            messages.success(request, "Password and Confirm Password are not same ! ")

         else:
            my_user1=User.objects.create_user(username2,email2,password2)
            my_user1.save()
            return redirect('login1')
    return render(request, 'index1.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request, "Incorrect Username or Password ! ")
            

    return render(request, 'login.html')

def LoginPage1(request):
    if request.method=='POST':
        usernam=request.POST.get('username2')
        passe=request.POST.get('pass2')
        usera=authenticate(request,username=usernam,password=passe)
        if usera is not None:
            login(request,usera)
            return redirect('home1')
        else:
            messages.success(request, "Incorrect Username or Password ! ")
            
    return render(request, 'login1.html')

    

def logoutPage(request):
    logout(request)
    return redirect('signup')


def ADD(request):
    if request.method== "POST":
    
        name= request.POST.get('name')
        type= request.POST.get('type')
        desc =request.POST.get('desc')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        dead = request.POST.get('dead')
        

        job = Jobs(
            name=name,
            type=type,
            desc=desc,
            address=address,
            phone=phone,
            dead=dead,
        )
        job.save()
    return redirect('home')

def Edit(request):
    job = Jobs.objects.all()

    context={
        'job':job,
    }
    return redirect (request,'home.html', context)

def Update(request, id):
    if request.method=="POST":
        name= request.POST.get('name')
        type= request.POST.get('type')
        desc =request.POST.get('desc')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        dead = request.POST.get('dead')
        

        job = Jobs(
       
            id=id,
            name=name,
            type=type,
            desc=desc,
            address=address,
            phone=phone,
            dead=dead,
        )
        job.save()
        return redirect ('home')
    

def Delete(request,id):
    job = Jobs.objects.filter(id=id)
    job.delete()
    context={
        'job':job,
    }
    return redirect ('home')


def manage_jobs(request):
    jobs=Jobs.objects.filter(user=request.user, name=request.user.name)
    context={'jobs':jobs}
    return render(request, 'manage_jobs.html', context)

def apply_to_job(request, id):
    if request.user.is_authenticated:
        job=Jobs.objects.get(id=id)
        ApplyJob.objects.create(
            job=job,
            user=request.user,
            status='pending'
        )
        messages.info(request, 'Applied Successfully !')
        return redirect('home1')
    else:
        messages.info(request, 'Please Login First !')
        return redirect('index1')
    
def Applications(request):
    job=ApplyJob.objects.filter(user=request.user)
    context={
        'job': job
    }
    return render(request, 'applications.html', context)
    


    





