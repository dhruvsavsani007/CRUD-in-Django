from django.db import models

# Create your models here.


class Students(models.Model):
    name = models.TextField()
    dec = models.TextField()
    img = models.ImageField(upload_to="student_img/")
