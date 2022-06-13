from django.db import models


class Card(models.Model):
     title = models.CharField(max_length=50)
     description = models.TextField()
     image = models.ImageField(upload_to='img/')


     def __str__(self):
         return f'{self.title}'