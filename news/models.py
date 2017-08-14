from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    category_name=models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class News(models.Model):
    title= models.CharField(max_length=200)
    content=models.CharField(max_length=750)
    author=models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE ,blank=True, null=True)
    pub_date = models.DateTimeField()

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title





