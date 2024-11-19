from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=1, unique=True)  # Regions A-G

    def __str__(self):
        return self.name


class Ticket(models.Model):
    datetime = models.DateTimeField()
    day_of_week = models.CharField(
        max_length=10)  # Store day name e.g., 'Monday'
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street_address} - {self.datetime}"
