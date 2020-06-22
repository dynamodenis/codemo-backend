from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='profiles', default='default.jpeg')
    location=models.CharField(max_length=100, blank=True)
    bio=models.TextField(blank=True)
    education=models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.user.username
    
    
