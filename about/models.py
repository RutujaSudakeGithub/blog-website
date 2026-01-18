from django.db import models

# Create your models here.

class About(models.Model):
    about_title = models.TextField(max_length=50)
    about_description = models.TextField(max_length=250)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateField(auto_now=True)


    class Meta:
        verbose_name_plural = 'about'

    def __str__(self):
        return self.about_title
    
class SocailLinks(models.Model):
    platfrom = models.CharField(max_length=25)
    link = models.URLField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platfrom

