from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    author = models.CharField(max_length=255)
    date = models.DateTimeField()

    def __str__(self):
        return self.title