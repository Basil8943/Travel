from django.db import models


class form(models.Model):
    img=models.ImageField(upload_to='pics')