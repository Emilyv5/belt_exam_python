from django.shortcuts import render, redirect
from django.contrib import messages
from login_registration.models import *
import bcrypt
import json
import login_registration.urls


def dashboard(request):
	if 'userid' in request.session:
		user = User.objects.get(id = request.session['userid'])
		jobs = Job.objects.filter(user_who_do__isnull=True)
		reverse_jobs = reversed(list(jobs))
		user_uploaded_jobs = user.jobs_uploaded.all()
		user_do_jobs = user.jobs_do.all()
		context = {
		'user' : user,
		'jobs': reverse_jobs,
		'self_upload': user_uploaded_jobs,
		'do_jobs' : user_do_jobs,

		}
		return render(request, 'dashboard.html', context)
	else:
		return redirect('/')

def jobs_new(request):

	return render(request, 'new.html')

def add_job(request):
	errors = Job.objects.basic_validator(request.POST)
	user = User.objects.get(id = request.session['userid'])

	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect("/jobs/new")

	catlist = request.POST.getlist('cat')
	to_cat = json.dumps(catlist)
	if len(errors) == 0:
		catlist = request.POST.getlist('cat')
		Job.objects.create(title =request.POST['title'], desc = request.POST['desc'], loc = request.POST['loc'], cat = to_cat, uploaded_by = user)

	return redirect('/dashboard')

def edit(request, num):
	user = User.objects.get(id = request.session['userid'])
	job = Job.objects.get(id = num)
	cat = job.cat
	cat = job.cat[1:-1]
	catlist = cat.split(",")
	context = {
	'user' : user,
	'job' : job,
	'cats' : catlist,
	'boolean' : job.user_who_do and job.user_who_do.id == user.id,
	}
	return render(request, 'show.html', context)

def edit_id(request, num):
	user = User.objects.get(id = request.session['userid'])
	job = Job.objects.get(id = num)

	context = {
	'user' : user,
	'job' : job,
	}
	return render(request, 'show_id.html', context)

def edition(request, num):
	errors = Job.objects.basic_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect("/jobs/edit/{}".format(num))
	job = Job.objects.get(id = num)
	job.title = request.POST['title']
	job.desc = request.POST['desc']
	job.loc = request.POST['loc']
	job.save()
	return redirect('/dashboard')

def add(request, num):
	user = User.objects.get(id = request.session['userid'])
	job = Job.objects.get(id = num)
	job.user_who_do = user
	job.save()
	return redirect('/dashboard')

def giveup(request, num):
	user = User.objects.get(id = request.session['userid'])
	job = Job.objects.get(id = num)
	job.user_who_do = None
	job.save()
	return redirect('/dashboard')

def jobadd(request, num):
	user = User.objects.get(id = request.session['userid'])
	job = Job.objects.get(id = num)
	job.user_who_do = user
	job.save()
	return redirect('/jobs/{}'.format(num))

def jobgiveup(request, num):
	user = User.objects.get(id = request.session['userid'])
	job = Job.objects.get(id = num)
	job.user_who_do = None
	job.save()
	return redirect('/jobs/{}'.format(num))

def delete(request, num):
	job = Job.objects.get(id = num)
	job.delete()
	return redirect('/dashboard')

def cancel(request):

	return redirect('/dashboard')

def logout(request):

	del request.session['userid']

	return redirect('/')


