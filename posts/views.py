from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import (
    Post,
    Comments
)



# Create your views here.


class ListPosts(View):
    template_name = "posts/posts.html"
    
    def get(self, request, spaceid):
        context = dict()
        context['posts'] = Post.objects.filter(space=spaceid)
        return render(request, self.template_name, context)
    
class PostDetail(View):
    template_name = "posts/postdetail.html"
    
    def get(self, request, pk):
        context = dict()
        context['post'] = Post.objects.get(id=pk)
        context['comments'] = Comments.objects.filter(post=context['post'])
        return render(request, self.template_name, context)
    
    def post(self, request, pk):
        text = request.POST['newcomment']
        post = Post.objects.get(id=pk)
        Comments.objects.create(text=text, user=request.user, post=post)
        return redirect(f"/posts/postdetail/{pk}/")
    
class CommentLike(View):
    
    def get(self, request, pk):
        comment = Comments.objects.get(id=pk)
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)
            
        return redirect(f"/posts/postdetail/{comment.post.id}/")
    
class CommentDislike(View):
    
    def get(self, request, pk):
        comment = Comments.objects.get(id=pk)
        if request.user in comment.dislikes.all():
            comment.dislikes.remove(request.user)
        else:
            comment.dislikes.add(request.user)
            
        return redirect(f"/posts/postdetail/{comment.post.id}/")
        