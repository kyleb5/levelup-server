from django.db import models


class Gamer(models.Model):

    uid = models.CharField(max_length=55, unique=True)
    bio = models.CharField(max_length=50)
