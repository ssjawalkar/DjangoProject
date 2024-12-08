from django.shortcuts import render, redirect
from .models import UserDetail
from django.http import HttpResponse
# Create your views here.
def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if not UserDetail.objects.filter(email=email).exists():
            UserDetail.objects.create(username=username,email=email,password=password)
            return redirect('login')
    return render(request,"signup.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        userValid = UserDetail.objects.filter(email=email, password=password).first()
        if userValid:
            return HttpResponse("Login Succeeful!!!")
    return render(request,"login.html")
