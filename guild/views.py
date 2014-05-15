from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from news import views

def my_login(request):
	print "in my_login"
	if not request.POST.get('username', False):
		raise Http404
	if not request.POST.get('password', False):
		raise Http404
		
	username = request.POST['username']
	password = request.POST['password']
	
	user = authenticate(username=username, password=password)
	
	if user is not None:
		login(request, user)
	return HttpResponseRedirect(reverse('news:news'))
		
def my_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('news:news'))