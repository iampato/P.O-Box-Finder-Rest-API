from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    box = models.TextField()
    mapurl = models.CharField(max_length=1000) 
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return '%s %s' % (self.title, self.body)