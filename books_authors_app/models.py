from django.db import models

# Create your models here.
class Book(models.Model):
     title = models.CharField(max_length=255)
     desc = models.TextField(default="")
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)

     def __str__ (self):
          return f"{self.title} {self.desc}"

class Author (models.Model):
     first_name = models.CharField(max_length=45)
     last_name = models.CharField(max_length=45)
     books = models.ManyToManyField(Book, related_name = 'authors')
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     notes = models.TextField(default="")

     def __str__ (self):
          return f"{self.first_name} {self.last_name}"