from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    excerpt=models.TextField(max_length=300)
    description=models.TextField()
    price=models.IntegerField(default=0)
    picture=models.ImageField(upload_to='img')
    digital = models.BooleanField(default=False,null=True, blank=True)
    
    def __str__(self):
        return self.name
    

