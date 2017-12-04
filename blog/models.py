from django.db import models
from django.conf import settings

class Publication(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__ (self):
      return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=50)


    def __str__ (self):
        return self.category_name


class Post(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=140,
                                blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    blog = models.ForeignKey(Publication)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ForeignKey(Category, null=True, blank=True)


    def __str__ (self):
        return self.title
