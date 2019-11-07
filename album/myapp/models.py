from django.db import models
from datetime import datetime

# Create your models here.
class Album(models.Model):
	name = models.CharField(max_length=20)
	title = models.CharField(max_length=20)
	addtime = models.DateTimeField(default=datetime.now)
