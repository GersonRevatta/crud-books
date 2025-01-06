from django.db import models
from bson import ObjectId

def generate_object_id():
    return str(ObjectId())

class Book(models.Model):
    id = models.CharField(max_length=24, primary_key=True, editable=False, default=generate_object_id)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    genre = models.CharField(max_length=100)
    price = models.FloatField()
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.published_date:
            self.year = self.published_date.year
        super().save(*args, **kwargs)
