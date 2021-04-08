
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if update_form.is_valid() and prof_form.is_valid():
            update_form.save()
            prof_form.save()
            messages.success(request, f'Your Account is updated')
            return redirect('profile')

    else:
        update_form = UserUpdateForm( instance=request.user)
        prof_form = ProfileUpdateForm( instance=request.user.profile)
    context = {
        'update_form': update_form,
        'prof_form': prof_form

    }
    return render(request, 'profile.html', context)
