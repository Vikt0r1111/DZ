from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post, Comment

def post_list(request):
    posts = Post.objects.all()
    # Додати логіку для пагінації
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    # Додати логіку для відображення деталей поста, коментарів та тегів
    return render(request, 'post_detail.html', {'post': post})