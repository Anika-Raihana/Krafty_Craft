from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse


from django.http import HttpResponse


from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


from App_Login.models import Profile
from App_Login.forms import UserProfileForm, SignUpForm


from django.contrib import messages

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations!! Your Account Has Been Created Successfully!")
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request, 'App_Login/sign_up.html', context={'form':form})


def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Shop:home'))
    return render(request, 'App_Login/login.html', context={'form':form})

@login_required
def user_logout(request):
    logout(request)
    messages.warning(request, "You have been logged out!!")
    return HttpResponseRedirect(reverse('App_Shop:home'))
   


@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = UserProfileForm(instance=profile)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your changes have been saved successfully!!")
            form = UserProfileForm(instance=profile)
    return render(request, 'App_Login/change_profile.html', context={'form':form})