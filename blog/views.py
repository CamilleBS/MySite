from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post

def detail(request, id):
    post = get_object_or_404(Post, pk=id) 
    return render(request,'blog/show.html',{'post':post})
