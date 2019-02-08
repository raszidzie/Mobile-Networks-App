from django.db import models
from django.utils.text import slugify
# Create your models here.
class Countries(models.Model):
    country_name = models.CharField(max_length=100)
    country_flag = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    
    def __str__(self):
        return self.country_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.country_name)
        return super(Countries, self).save(*args, **kwargs)      

class Operators(models.Model):

    operator_name = models.CharField(max_length=100)
    operator_description = models.TextField(blank=True)
    image = models.FileField(null=True, blank=True )
    slug = models.SlugField(unique=True, max_length=100)
    country = models.ForeignKey('mobile.Countries', related_name='operators', on_delete=models.CASCADE) 

    def __str__(self):
        return self.operator_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.operator_name)
        return super(Operators, self).save(*args, **kwargs)    