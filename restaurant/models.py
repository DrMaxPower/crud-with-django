from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Booking(models.Model):
    """
    data information from costumers about booking table
    """
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    guests = models.PositiveSmallIntegerField()
    date = models.DateTimeField()
    info = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.fname} {self.lname} day: {self.date}"


class Menu(models.Model):
    """  """
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()

    def __str__(self):
        return self.title



