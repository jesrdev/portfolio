from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):
    image = CloudinaryField('image', null=True)
    summary = models.CharField(max_length=200)
    specifics = models.TextField(blank = True)
    app_url = models.CharField(max_length=100)

    def __str__(self):
        return self.summary