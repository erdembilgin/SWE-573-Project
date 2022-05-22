from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import User
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def index(request):
    return HttpResponse("working")

class LoginView(View):
    template_name = "accounts/login.html"
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("spaces/home")
        return render(request, self.template_name)
    
    def post(self, request):
        print("in post")
        email = request.POST['email']
        pwd = request.POST['pwd']
        user = authenticate(email=email, password=pwd)
        if user is not None:
            login(request, user)
        else:
            return redirect("/")
        print(user)
        return redirect("spaces/home")
    
class LogoutView(View):
    
    def get(self, request):
        logout(request)
        return redirect("/")
    
class RegisterView(View):
    template_name = "accounts/signup.html"
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("spaces/home")
        return render(request, self.template_name)
    
    def post(self, request):
        image = request.FILES['avatar']
        nickname = request.POST['nickname']
        email = request.POST['email']
        pwd = request.POST['pwd']
        user = User.objects.create(email=email, nick_name=nickname, profile_photo=image)
        user.set_password(pwd)
        user.save()
        print(request.FILES['avatar'])
        print(request.POST['nickname'])
        print(request.POST['email'])
        print(request.POST['pwd'])
        return redirect("/")
    
class Profile(View):
    template_name = "accounts/profile.html"
    
    def get(self, request):
        if request.user.is_authenticated:
            context = dict()
            context['user'] = request.user
            return render(request, self.template_name, context)
        return redirect("/")

class ChangePassword(View):
    template_name = "accounts/changepassword.html"
    
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
    
        return redirect("/")
    
    def post(self, request):
        oldpwd = request.POST['oldpwd']
        newpwd = request.POST['newpwd']
        
        if request.user.check_password(oldpwd):
            request.user.set_password(newpwd)
            request.user.save()
            return redirect("/profile")
        return redirect("/")