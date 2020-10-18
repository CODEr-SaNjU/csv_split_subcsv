from django.db import models

# Create your models here.

class Documents(models.Model):
    document = models.FileField(upload_to='uploads/')