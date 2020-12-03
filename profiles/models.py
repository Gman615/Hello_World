from django.db import models

TYPE_CHOICES = {
    ('Mr','Mr'),
    ('Mrs','Mrs'),
    ('Ms','Ms'),
}

class Profiles(models.Model):
    Prefix = models.CharField(max_length=60, choices=TYPE_CHOICES, default="---------")
    First_Name = models.CharField(max_length=60, default="")
    Last_Name = models.CharField(max_length=60, default="")
    Email = models.CharField(max_length=60, default="")
    Username = models.CharField(max_length=60, default="")

    objects = models.Manager()

    def __str__(self):
        return self.Username