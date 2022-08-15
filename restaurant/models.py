from django.db import models


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
    info = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.fname} {self.lname} day: {self.date}"
