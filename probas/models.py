from django.db import models

class Person(models.Model):
    """This is a demo person model"""

    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    picture = models.ImageField(null=True)
