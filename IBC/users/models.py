from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=8, unique=True, help_text='Max of 8 Characters')
    image = models.ImageField()
    date_of_birth = models.DateField()
    slug = models.SlugField(primary_key=True)
    gender = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    level = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.username}"
