from django.shortcuts import render, redirect
from django.contrib import messages
from login_registration.models import *
import bcrypt
import handy_helper.urls


def index(request):

	if 'invalid' in request.session:
		context = {
		'wrong' : request.session['invalid'],
		}
		return render(request, 'index.html', context)
	else:
		return render(request, 'index.html')


def addition(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect("/")

	if not User.objects.filter(email = request.POST['email']).exists():
		password = request.POST['password']
		pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
		User.objects.create(first_name =request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password =pw_hash )

	return redirect('/')

def check(request):

	errors = User.objects.login_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect("/")

	user = User.objects.filter(email = request.POST['email'])

	if user:
		logged_user = user[0]
		if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
			request.session['userid'] = logged_user.id
			del request.session['invalid']
			return redirect('/dashboard')
		else:
			request.session['invalid'] = 'Invalid match'
	
	return redirect('/')















