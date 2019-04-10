from .models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)                 # here we creating a form and save the data we entered
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You may log in ')
            return redirect('login')                        # after we submit the form we will go back to home page
    else:
        form = UserRegisterForm()                             # if its not a valid post request we create a blank form
    return render(request, 'users/register.html', {'form': form})

@login_required                                               # user must be logged in to view this page!
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

