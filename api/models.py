from django.db import models

# Create your models here.
class School(models.Model):
    title = models.CharField(max_length=200)
    box = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return '%s %s' % (self.title, self.body)