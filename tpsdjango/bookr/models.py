# Create your models here.
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey('BookType', on_delete=models.CASCADE)
    status = models.ForeignKey('BookStatus', on_delete=models.CASCADE)

    def __unicode__(self):
        return f"{self.name} [{self.price}]"
    
class BookType(models.Model):
    category = models.CharField(max_length=100)
    
    def __unicode__(self):
        return f"{self.category}"

class BookStatus(models.Model):
    status = models.CharField(max_length=100)

    def __unicode__(self):
        return f"{self.status}"
