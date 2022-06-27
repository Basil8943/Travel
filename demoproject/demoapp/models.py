from django.db import models

# Create your models here.
class shop(models.Model):
    dist=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.dist
class background(models.Model):
    name=models.CharField(max_length=100)
    back=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name
class traditional(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='trad')
    desc=models.TextField()
    def __str__(self):
        return self.name
class kerala(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
