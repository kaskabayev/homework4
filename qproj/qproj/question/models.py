from django.db import models
from django.utils import timezone

class Question(models.Model):
	text = models.CharField(max_length=1000)
	pub_time = models.DateTimeField(auto_now_add=timezone.now)
	is_public = models.BooleanField(default=False)