from __future__ import unicode_literals
from django.db import models
import json
import re


class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if len(postData['first_name']) < 2:
			errors['firstname'] = 'First name must be at least 2 characters'
		if len(postData['last_name']) < 2:
			errors['lasttname'] = 'Last name must be at least 2 characters'
		if len(postData['password']) < 8:
			errors['password'] = 'Password must be at least 8 characters'
		if postData['password'] != postData['confirm_password']:
			errors['confirm_password'] = 'confirm password is not matched'
		if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = ("Invalid email address!")
		return errors

	def login_validator(self, postData):
		errors = {}
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if len(postData['password']) < 8:
			errors['password'] = 'Password must be at least 8 characters'
		if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = ("Invalid email address!")
		return errors

class User(models.Model):
	first_name = models.CharField(max_length = 45)
	last_name = models.CharField(max_length = 45)
	email = models.CharField(max_length = 45)
	password = models.CharField(max_length = 45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	# jobs_uploaded
	# jobs_do
	objects = UserManager()

class JobManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['title']) < 3:
			errors['title'] = 'title must be at least 3 characters'
		if len(postData['desc']) < 3:
			errors['desc'] = 'Description must be at least 3 characters'
		if len(postData['loc']) < 3:
			errors['loc'] = 'Locations must be at least 3 characters'
		return errors


class Job(models.Model):
	title = models.CharField(max_length = 45)
	desc = models.TextField()
	loc = models.CharField(max_length = 45)
	cat = models. CharField(max_length = 45)
	uploaded_by = models.ForeignKey(User, related_name = 'jobs_uploaded', on_delete = models.CASCADE)
	user_who_do = models.ForeignKey(User, related_name = 'jobs_do', on_delete = models.CASCADE, null = True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = JobManager()

# class JobManager(models.Manager):
# 	def basic_validator(self, postData):
# 		errors = {}
# 		if len(postData['title']) == 0:
# 			errors['title'] = 'title can not be blank'
# 		if len(postData['desc']) < 5:
# 			errors['desc'] = 'Description must be at least 5 characters'
# 		return errors




# class Book(models.Model):
# 	title = models.CharField(max_length=255)
# 	desc = models.TextField()
# 	uploaded_by = models.ForeignKey(User, related_name = "books_uploaded", on_delete = models.CASCADE)
# 	users_who_like = models.ManyToManyField(User, related_name = 'liked_books')
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)

# 	objects = BookManager()