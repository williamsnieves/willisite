from django.forms import ModelForm
from django import forms
from messages.models import Message


class MessageForm(ModelForm):
	class Meta:
		model = Message
		fields = ['name']