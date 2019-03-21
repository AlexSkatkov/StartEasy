from django.shortcuts import render
from .models import Post
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404
from users.forms import ContactForm
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone

# we send the user to the suitable template to view the page with a title


def home(request):
    if request.user.is_authenticated:
        context = {
            #'posts': Post.objects.all()
            'posts': Post.objects.filter(author=request.user)  #  a query that gets all the the posts from the database(video5)
        }

        return render(request, 'project/home.html', context)
    return redirect('login')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'project/post_edit.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'project/post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'project/post_edit.html', {'form': form})