from django.db import models
# Create your models here.


# class Image(models.Model):
#     name=models.CharField(max_length=50)
#     image=models.ImageField(upload_to='images/')
    
#     def __str__(self):
#         return str(self.id)
class ImageSet(models.Model):
    img = models.ImageField(upload_to = "images/")
    #def save(self, *args , **kwargs):
    #    return super().save(*args,**kwargs)    
  