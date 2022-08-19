from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

class Booking(models.Model):
    """
    data information from costumers about booking table
    """
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    guests = models.PositiveSmallIntegerField(blank=True, null=True)
    date = models.DateTimeField()
    info = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.fname} {self.lname} {self.date}"


FOOD_TYPE = (
    ('breakfast', 'breakfast'),
    ('lunch', 'lunch'),
    ('dinner', 'dinner'),
)

class Menu(models.Model):
    """  """
    type = models.CharField(
        max_length=100, 
        choices=FOOD_TYPE,
        default="lunch")
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100)
    price = models.DecimalField(
        blank=True,
        null=True,
        max_digits=5,
        decimal_places=2
        )
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()


    class Meta:
        ordering = ['type', 'price']


    def __str__(self):
        return self.title

