from django.shortcuts import get_object_or_404, render_to_response,render
from django.template import RequestContext, loader

# Create your views here.

def home(request):
	return render_to_response('home.html')


