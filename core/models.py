from django.db import models
from django.contrib.auth.models import User

class Provider(models.Model):
    """
    A provider is a Course provider, like
    Codeschool, Pluralsight ...
    """
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Status(models.Model):
    """
    Each Course has an status:
    completed  or in_progress
    """
    STATUS_CHOICES = (
        ('c', 'completed'),
        ('i', 'in_progress'),
    )
    name = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        """ I know this is bullshit, I need to fix this"""
        if self.name == 'c':
            return 'completed'
        if self.name == 'i':
            return 'in_progress'


class Course(models.Model):
    """
    Each course of each Provider
    """
    title = models.CharField(max_length=128, blank=True)
    url = models.CharField(max_length=256, blank=True)
    badge = models.CharField(max_length=256, blank=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Bio(models.Model):
    """
    More info about the user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=512, blank=True)
    description = models.CharField(max_length=32, blank=True)
    resume = models.CharField(max_length=32, blank=True)
    birth_date = models.DateField(null=True, blank=True)



class ProviderProfile(models.Model):
    """
    Profile of the user in each Provider.
    The user will tipically have an account for
    each provider.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username_provider = models.CharField(max_length=30, blank=True)
    courses = models.ManyToManyField(Course, through='CourseStatus')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.provider)

class CourseStatus(models.Model):
    """
    Each course of each profile has an status
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    profile = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
