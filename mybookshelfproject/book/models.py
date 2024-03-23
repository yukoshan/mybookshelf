from django.db import models
from datetime import date

from .consts import MAX_RATE

CATEGORY = (('novel', '小説'), ('essay', 'エッセイ'), ('practical', '実用書'))

RATE_CHOICES = [(x, str(x)) for x in range(1, MAX_RATE + 1)]

class Book(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=100)
    author = models.TextField(max_length=100)
    models.DateField(default=date.today)
    rate = models.IntegerField(choices=RATE_CHOICES, null=True)
    category = models.CharField(
        max_length=100,
        choices = CATEGORY
        )
    text = models.TextField(max_length=2000,null=True)

    
    def __str__(self):
        return self.title
    