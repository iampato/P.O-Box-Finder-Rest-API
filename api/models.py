from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    box = models.CharField(max_length=400)
    mapurl = models.CharField(max_length=300) 
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.title