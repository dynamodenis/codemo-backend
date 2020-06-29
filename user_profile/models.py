from django.db import models
from django.conf import settings
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    picture=models.ImageField(upload_to='profiles', default='default.jpeg',blank=True)
    location=models.CharField(max_length=100, blank=True)
    bio=models.TextField(blank=True)
    education=models.CharField(max_length=50, blank=True)
    company=models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return self.user.username
    
    def save(self,*args,**kwargs):
        super().save()
        
        img=Image.open(self.picture.path)
        
        if img.height>400 and img.width>400:
            size=(400,400)
            img.thumbnail(size)
            img.save(self.picture.path)
    
    
    
class Test(models.Model):
    name=models.CharField(max_length=20)
    profile=models.ForeignKey(Profile ,on_delete=models.CASCADE)

