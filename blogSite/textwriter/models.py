from django.db import models
from blogapp.models import Categories
from tinymce.models import HTMLField


class Textwriter(models.Model):
    Book_category = models.ForeignKey(Categories,on_delete=models.CASCADE , null=False , )
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    coverImage = models.ImageField(upload_to='images/')
    body = HTMLField(blank=True , null = True )
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

# Create your models here.
