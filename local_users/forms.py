from allauth.account.forms import SignupForm
from .models import Profile, User
from django import forms

GENDER = (('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other'),)


class CustomSignupForm(SignupForm):
    phone_number = forms.CharField(max_length=12, label='Phone Number')
    gender = forms.MultipleChoiceField(choices=GENDER)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.phone_number = self.cleaned_data['phone_number']
        user.gender = self.cleaned_data['gender']
        user.save()
        return user
