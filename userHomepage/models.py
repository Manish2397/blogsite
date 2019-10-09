from django.db import models

# Create your models here.

class blog(models.Model):
    user = models.CharField(max_length=30)
    blog = models.TextField(max_length=2000)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    Science = models.BooleanField()
    Math = models.BooleanField()
    History =models.BooleanField()
    Programming = models.BooleanField()
    cs = models.BooleanField()
    cpp= models.BooleanField()
    ml = models.BooleanField()
    iot =models.BooleanField()
    Robots = models.BooleanField()
    Space = models.BooleanField()
    Literature = models.BooleanField()
    appD=models.BooleanField()
    Political = models.BooleanField()
    Sports =models.BooleanField()
    Cricket =models.BooleanField()
    Bollywood=models.BooleanField()
    Hollywood=models.BooleanField()
    TV=models.BooleanField()
    Life=models.BooleanField()
    public = models.BooleanField()
    private = models.BooleanField()
    
