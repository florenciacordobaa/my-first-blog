from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    ceated_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField( blank= True, null= True )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #__ = "dunder" (diminutivo en inglés de "double-underscore").
    def __str__(self):
        return self.title
