from django.shortcuts import render
from .models import Post 
from rest_framework import permissions, viewsets

from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.

def homepage(request):
    posts = Post.objects.all() 
    return render(request, 'blog/home.html', {'posts': posts})

