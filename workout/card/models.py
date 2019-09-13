from django.db import models

# Create your models here.


class Weight(models.Model):
    type = models.CharField(max_length=255, blank=True, null=True)
    pounds = models.IntegerField(blank=True, null=True)

    # this is a method on the class
    # methods always get passed in self
    def __str__(self):
        return self.type


class Card(models.Model):
    excercise = models.CharField(max_length=255, blank=True, null=True)
    weight = models.ForeignKey(
        Weight, on_delete=models.DO_NOTHING, blank=True, null=True)
