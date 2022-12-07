from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm, UpdateUserForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView


# Create your views here.


@login_required(login_url='account_login')
def profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    context = {
        'profile': profile
    }
    print(f"My image is {profile.bio}")
    return render(request, './profile.html', context)


@login_required(login_url='account_login')
def update_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    profile_form = ProfileForm(instance=profile)
    user_form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=profile)
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('profile')

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(request, 'update_profile.html', context)


class CustomChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'account/password_change.html'
    success_url = "profile"
