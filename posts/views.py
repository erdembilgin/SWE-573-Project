from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import (
    Post,
    Comments
)

from spaces.models import (
    Space
)



# Create your views here.


class ListPosts(View):
    template_name = "posts/posts.html"
    
    def get(self, request, spaceid):
        if request.user.is_authenticated:
            
            context = dict()
            context['posts'] = Post.objects.filter(space=spaceid)
            spaceuser = Space.objects.get(id=spaceid).user.all()
            if request.user in spaceuser:
                context['button'] = True
                context['spaceid'] = spaceid
            return render(request, self.template_name, context)
        return redirect("/")
    
    def post(self, request, spaceid):
        if request.user.is_authenticated:
            search_word = request.POST['searchposts']
            context = dict()
            print("this is space id ", spaceid)
            context['posts'] = Post.objects.filter(title__contains=search_word, space=spaceid)
            spaceuser = Space.objects.get(id=spaceid).user.all()
            if not context['posts'].exists():
                context['emptymsg'] = "No post could be found"
            if request.user in spaceuser:
                context['button'] = True
                context['spaceid'] = spaceid
            return render(request, self.template_name, context)    
        
        return redirect("/")
    
class PostDetail(View):
    template_name = "posts/postdetail.html"
    
    def get(self, request, pk):
        if request.user.is_authenticated:
            context = dict()
            context['post'] = Post.objects.get(id=pk)
            context['comments'] = Comments.objects.filter(post=context['post'])
            return render(request, self.template_name, context)
    
        return redirect("/")
    
    def post(self, request, pk):
        text = request.POST['newcomment']
        post = Post.objects.get(id=pk)
        Comments.objects.create(text=text, user=request.user, post=post)
        return redirect(f"/posts/postdetail/{pk}/")
    
class CommentLike(View):
    
    def get(self, request, pk):
        if request.user.is_authenticated:
            comment = Comments.objects.get(id=pk)
            if request.user in comment.likes.all():
                comment.likes.remove(request.user)
            else:
                comment.likes.add(request.user)
                
            return redirect(f"/posts/postdetail/{comment.post.id}/")
        return redirect("/")
    
class CommentDislike(View):
    
    def get(self, request, pk):
        if request.user.is_authenticated:
            comment = Comments.objects.get(id=pk)
            if request.user in comment.dislikes.all():
                comment.dislikes.remove(request.user)
            else:
                comment.dislikes.add(request.user)
                
            return redirect(f"/posts/postdetail/{comment.post.id}/")
        return redirect("/")
    
class CreatePost(View):
    template_name = "posts/createpost.html"
    
    def get(self, request, spaceid):
        if request.user.is_authenticated:
            return render(request, self.template_name)
    
        return redirect("/")
    
    def post(self, request, spaceid):
        title = request.POST['title']
        description = request.POST['description']
        try:
            img = request.FILES['img']
        except Exception as e:
            img = None
        try:
            video = request.FILES['video']
        except Exception as e:
            video = None
        
        space = Space.objects.get(id=spaceid)
        post = Post.objects.create(title=title, description=description, image=img, 
                                   video=video, space=space, user=request.user)
        return redirect(f"/posts/{spaceid}")
    
class DeletePost(View):
    
    def get(self, request, pk):
        if request.user.is_authenticated:
            post = Post.objects.get(id=pk)
            spaceid = post.space.id
            post.delete()
            return redirect(f"/posts/{spaceid}")
        return redirect("/")
        
        