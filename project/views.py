from django.shortcuts import render
from .models import Post
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404
from users.forms import ContactForm
from .forms import PostForm,PostForm2, CommentForm
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django_xhtml2pdf.utils import generate_pdf

# we send the user to the suitable template to view the page with a title

from PyPDF2 import PdfFileMerger


def pdf(request):
    resp = HttpResponse(content_type='project/pdf')
    context = {
        'post': Post.objects.all()
    }
    result = generate_pdf('project/pdf.html', file_object=resp, context=context)
    return result

def home(request):
    if request.user.is_authenticated:
        context = {
            #'posts': Post.objects.all()
            'posts': Post.objects.filter(author=request.user) | Post.objects.filter(user1=request.user.username) | Post.objects.filter(user2=request.user.username) |
                     Post.objects.filter(user3=request.user.username) | Post.objects.filter(user4=request.user.username) | Post.objects.filter(client=request.user.username)
            #  a query that gets all the the posts from the database(video5)
        }

        return render(request, 'project/home.html', context)
    return redirect('login')


def post_new(request):
    if request.method == "POST":
        form = PostForm2(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm2()
    return render(request, 'project/post_edit.html', {'form': form})

def tips(request):
    return render(request, 'project/tips.html')

def about(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'project/About.html', {'form': form})

def help(request):
    return render(request, 'project/help.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'project/post_detail.html', {'post': post})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if (request.user.username != str(post.author)):
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
    else:
        if request.method == "POST":
            form = PostForm2(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm2(instance=post)
    return render(request, 'project/post_edit.html', {'form': form})

def post_delete(request,pk):
        post = get_object_or_404(Post, pk=pk)
        creator = post.author
        if request.user.is_authenticated and (request.user.username == str(creator)):
            post.delete()
            messages.success(request, "Post successfully deleted!")
            #return HttpResponseRedirect('project/home.html')
            return render(request, 'project/home.html')
        context = {'post': post,
                   'creator': creator,
                   }
        messages.error(request, "Post cannot be deleted by you")
        return render(request, 'project/home.html')

def examples(request):
    return render(request, 'project/examples.html')


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'project/add_comment_to_post.html', {'form': form})