from django.contrib.auth.models import User

from django.db import models

from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from hello.utils import unique_slug_generator


class Class(models.Model):

    slug = models.SlugField(max_length=250, null=True, blank=True)



    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("adhyapna", kwargs={"slug":self.slug})


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Class)

class Topic(models.Model):
    """Name of topic a user is learning about"""
    image = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text

class Entry(models.Model):
    """Something specific learned about"""
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        return self.text[:50] + "..."


class Blog(models.Model):
    #image = models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    image = models.CharField(max_length=1000)
    txt = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    instructor = models.CharField(max_length=150)
    rating = models.CharField(max_length=150)
    duration = models.CharField(max_length=150)
    url = models.CharField(max_length=1000)

    def __str__(self):
        """Return a string representation of the model"""
        return self.txt[:50] + "..."





