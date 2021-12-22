from django.db import models


# Create your models here.
class BookType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=200, help_text='Max text length is 200')
    books = models.ManyToManyField('Book')

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(unique=True, primary_key=True)
    stars = models.SmallIntegerField()
    story = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"