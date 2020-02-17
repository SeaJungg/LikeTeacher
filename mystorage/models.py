from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class Essay(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete = models.CASCADE)
    title = models.CharField(max_length= 30)
    body = models.TextField()
    school = models.CharField(max_length=30, default= "ERICA")
    lecture = models.CharField(max_length= 30, default="데이터구조론")
    score = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], default=0)

class Album(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete = models.CASCADE)
    image = models.ImageField(upload_to="images")
    desc = models.CharField(max_length= 100)

class Files(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete = models.CASCADE)
    myfile = models.FileField(blank=False, null=False, upload_to = "files")
    desc = models.CharField(max_length= 100)