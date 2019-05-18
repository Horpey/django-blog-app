from django.shortcuts import render
from django.http import HttpResponse
# Import Data from Model
from .models import Post

# Create your views here.

def homepage(request):
    # posts = Post.objects.all()
    posts = Post.objects.order_by('-id')

    # posts = Post.objects.filter(title='My First Post')
    # posts = Post.objects.exclude()
    header = 'Welcome to my Blog'

    # print (posts)
    return render(request, 'index.html', {'titles': posts, 'header': header})
    # return HttpResponse('<h1>Hello World</h1>')