from django.forms import ModelForm
from django import forms
from categories.models import Category


class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = ['name']