from django.db import models

# Create your models here.
class Plate(models.Model):
    plate_num = models.FileField(upload_to = './upload')

