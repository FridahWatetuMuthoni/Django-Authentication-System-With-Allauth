from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from allauth.account.views import PasswordChangeView


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


class CustomPasswordChangeView(PasswordChangeView):
    success_url = 'profile'


"""
from profile import views
...
    url(r'accounts/password/change', views.custom_password_change),
    url(r'^accounts/', include('allauth.urls')),

    class CustomPasswordChangeView(PasswordChangeView):
    
    @property
    def success_url(self):
        print 'start'
        return '/unknown/'

custom_password_change = login_required(CustomPasswordChangeView.as_view())
"""
