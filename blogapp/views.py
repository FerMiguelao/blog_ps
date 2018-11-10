from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/home.html', {'posts':posts})

def post_completo(request, pk):
    posts = Post.objects.all()
    post_c = get_object_or_404(Post, pk=pk)
    return render(request, 'blogapp/post_completo.html', {'post_c':post_c,'posts':posts})
