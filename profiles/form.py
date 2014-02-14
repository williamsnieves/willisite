from django.forms import ModelForm
from django import forms
from profiles.models import Profile


class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['name']