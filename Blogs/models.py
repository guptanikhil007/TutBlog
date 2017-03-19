from django.db import models

from User.models import Profile
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	created = models.DateField(db_index=True, auto_now_add=True)
	category = models.ManyToManyField(Category)
	updated = models.DateField(db_index=True, auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ("blog-detail", [self.slug,])

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Blog, self).save(*args, **kwargs)

class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True, unique=True)
	def __str__(self):
		return self.title
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)

class Comment(models.Model):
	text = models.TextField()
	blog = models.ForeignKey(Blog)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateFieldauto_now=True)

	def __str__(self):
		return self.text

