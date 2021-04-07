from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



class About(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('about-detail', kwargs={'pk': self.pk})



class Wedo(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('wedo-detail', kwargs={'pk': self.pk})



class WeCanHelp(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('wecanhelp-detail', kwargs={'pk': self.pk})



class OurServices(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('ourservices-detail', kwargs={'pk': self.pk})



class ApeaMembership(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('apeamembership-detail', kwargs={'pk': self.pk})



class JoinUs(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('joinus-detail', kwargs={'pk': self.pk})


class PublicPolicy(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('publicpolicy-detail', kwargs={'pk': self.pk})



class MyWorkplace(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('myworkplace-detail', kwargs={'pk': self.pk})



class ApeaMember(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('apeamember-detail', kwargs={'pk': self.pk})




