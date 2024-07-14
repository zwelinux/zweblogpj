from django.shortcuts import render
from .models import Post 

# Create your views here.

def homepage(request):
    posts = Post.objects.all() 
    return render(request, 'blog/home.html', {'posts': posts})

