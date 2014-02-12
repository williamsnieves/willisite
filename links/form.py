from django.forms import ModelForm
from django import forms
from links.models import Link


class LinkForm(ModelForm):
	class Meta:
		model = Link
		fields = ['name']