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


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5},), required=False)

    class Meta:
        model = Profile
        fields = ['bio', 'image']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(
        max_length=12, label='Phone Number', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(
        choices=GENDER, required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'gender']
