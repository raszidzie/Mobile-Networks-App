from django.db import models

# Create your models here.
class Countries(models.Model):
    country_name = models.CharField(max_length=100)
    country_flag = models.CharField(max_length=100)
    
   
    


    def __str__(self):
        return self.country_name

class Operators(models.Model):

    operator_name = models.CharField(max_length=100)
    operator_description = models.TextField()
    image = models.FileField(null=True, blank=True )
    country = models.ForeignKey('mobile.Countries', related_name='operators', on_delete=models.CASCADE) 
  



    def __str__(self):
        return self.operator_name
        