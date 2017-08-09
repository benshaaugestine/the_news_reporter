from django.db import models
from django.utils import timezone
class News(models.Model):
    title= models.CharField(max_length=200)
    content=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    pub_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


    class Meta:
        ordering = ["pub_date"]
        get_latest_by = "pub_date"





