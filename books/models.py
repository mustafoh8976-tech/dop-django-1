from django.db import models


class Books(models.Model):
    name_b = models.CharField(max_length=200)
    after_b=models.CharField(max_length=150)
    caption=models.IntegerField()