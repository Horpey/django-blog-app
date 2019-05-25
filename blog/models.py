from django.db import models
# Importing Settings in Django
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Post(models.Model):
    author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    published = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null = True)

    def __str__(self):
        return '{} published on {}' .format(self.title, self.published.strftime("%d %B, %Y"))

class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name = 'comments')
    author = models.CharField(max_length = 50)
    body = models.TextField()
    active = models.BooleanField(default=True)
    published = models.DateTimeField(auto_now_add = True)
