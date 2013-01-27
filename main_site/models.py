from django.db import models

# Create your models here.

class Header(models.Model):
	heading = models.CharField(max_length=1000)
	background_image_url = models.URLField()
	title_image_url = models.URLField()
	title_image_url.blank = True
	title_text = models.CharField(max_length=100)
	title_text.blank = True

class Post(models.Model):
	title = models.CharField(max_length=1000)
	date_posted = models.DateField()
	image_url = models.URLField()
	story_header = models.CharField(max_length=2000)
	story_header.blank = True
	story_text = models.TextField()
	story_text.blank = True

	def __unicode__(self):
		return str(self.title)

class Shared_Images(models.Model):
	image_url = models.URLField()
	message = models.TextField()
