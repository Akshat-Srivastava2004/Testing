from django.shortcuts import render,redirect
from django.contrib.auth.models import User
def Home(request):
    return render(request,'Home.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        new_student=User.objects.create(
            username=username
        )
        new_student.set_password(password)
        new_student.save()
        return redirect('login')
    return render(request,'Home.html')