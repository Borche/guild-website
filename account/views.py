from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.models import User
from account.models import InvitationCode

# Create your views here.

def register(request):
	if request.method == 'POST':
		try:
			# Invitation code, needed to register
			code = request.POST['invitation_code']
			
			codes = InvitationCode.objects.all()
			code_is_valid = False
			inv_code = None
			for c in codes:
				if code == c.code:
					code_is_valid = True
					inv_code = c
					break
			
			if code_is_valid == False:
				return render(request, 'account/register.html', { 'error_message': 'Invalid invitation code.' })
			
			username = request.POST['username']
			password = request.POST['password']
			password_repeated = request.POST['password_repeated']
			
			if password != password_repeated:
				return render(request, 'account/register.html', { 'error_message': 'Passwords must be identical.' })
			
			email = request.POST['email']
			
			if len(email) < 5:
				return render(request, 'account/register.html', { 'error_message': 'Invalid email.' })
				
			if len(password) < 6:
				return render(request, 'account/register.html', { 'error_message': 'Password must be at least 6 characters long.' })
				
			if len(username) < 3:
				return render(request, 'account/register.html', { 'error_message': 'Username must be at least 3 characters long.' })
			
			users = User.objects.all()
			for u in users:
				if email == u.email:
					return render(request, 'account/register.html', { 'error_message': 'That email is already registered to an account.' })
			
			user = User.objects.create_user(username=username, password=password, email=email)
			user.save()
			inv_code.delete()
			return render(request, 'account/thanks.html')
		except Exception as e:
			raise e
			
def registration_page(request):
	return render(request, 'account/register.html')