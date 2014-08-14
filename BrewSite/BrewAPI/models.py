from django.db import models


class Brew(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=10)