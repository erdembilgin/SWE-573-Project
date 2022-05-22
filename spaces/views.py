from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import (
    Space
)



# Create your views here.


class HomeView(View):
    template_name = "spaces/homepage.html"
    
    def get(self, request):
        print("in spaces")
        if request.user.is_authenticated:
            context = dict()
            context['spaces'] = Space.objects.all()
            print("auth user")
            return render(request, self.template_name, context)    
        return redirect("/")
    
class JoinSpace(View):
    
    def get(self, request, pk):
        if request.user.is_authenticated:
            desired_space = Space.objects.get(id=pk)
            desired_space.user.add(request.user)
            print(desired_space.user.all())
            return redirect("/spaces/home")
        return redirect("/")
    
class LeaveSpace(View):
    
    def get(self, request, pk):
        if request.user.is_authenticated:
            desired_space = Space.objects.get(id=pk)
            desired_space.user.remove(request.user)
            print(desired_space.user.all())
            return redirect("/spaces/home")
        return redirect("/")
    
class CreateSpace(View):
    template_name = "spaces/newspace.html"
    
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        return redirect("/")
    
    def post(self, request):
        title = request.POST['title']
        description = request.POST['description']
        tags = request.POST['tags']
        img = request.FILES['banner']
        
        Space.objects.create(title=title, description=description, tags=tags, banner=img)
        return redirect("/spaces/home")