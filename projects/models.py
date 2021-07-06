from django.db import models

# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='static/')
    summary = models.CharField(max_length=200)
    specifics = models.CharField(max_length=200)
    app_url = models.CharField(max_length=100)
    image_name = models.CharField(max_length=50)

    def __str__(self):
        return self.summary