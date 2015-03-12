from django.utils import timezone
from django.db import models

class Post(models.Model):
	author = models.CharField(max_length = 1000)
	title = models.CharField(max_length = 1000)
	text = models.CharField(max_length = 1000)
	pub_date = models.DateTimeField(auto_now_add = timezone.now)
	upd_date = models.DateTimeField(auto_now = timezone.now)
	is_public = models.BooleanField(default = True)

class Comment(models.Model):
	author = models.CharField(max_length = 1000)
	text = models.CharField(max_length = 1000)
	pub_date = models.DateTimeField(auto_now_add = timezone.now)
	post = models.ForeignKey(Post)
