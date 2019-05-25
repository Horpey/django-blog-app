from django.shortcuts import render
from django.http import HttpResponse
# Import Data from Model
from .models import Post
from .forms import commentForm
# Create your views here.

def homepage(request):
    # posts = Post.objects.all()
    posts = Post.objects.order_by('-id')

    # posts = Post.objects.filter(title='My First Post')
    # posts = Post.objects.exclude()
    header = 'Collabtix Blog App'

    # print (posts)
    return render(request, 'index.html', {'titles': posts, 'header': header})
    # return HttpResponse('<h1>Hello World</h1>')

def singlepost (request, post_id):
    # To Retreive Object
    post = Post.objects.get(id = post_id)
    form = commentForm(request.POST)

    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
    # To get Comments
    comments = post.comments.all()

    return render(request, 'singlepost.html', {'post':post, 'form': form, 'comments': comments })