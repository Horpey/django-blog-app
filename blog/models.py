from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    published = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null = True)

    def __str__(self):
        return '{} published on {}' .format(self.title, self.published.strftime("%d %B, %Y"))

