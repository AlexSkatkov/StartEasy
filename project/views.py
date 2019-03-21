from django.shortcuts import render
from .models import Post
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from users.forms import ContactForm

# we send the user to the suitable template to view the page with a title


def home(request):
    context = {
        'posts': Post.objects.all()                      # a query that gets all the the posts from the database(video5)
    }
    return render(request, 'project/home.html', context)

