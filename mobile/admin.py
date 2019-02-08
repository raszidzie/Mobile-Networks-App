from django.contrib import admin
from .models import *
# Register your models here.

class CountryAdmin(admin.ModelAdmin):
    list_display = ['country_name', 'country_flag', 'slug']
    prepopulated_fields = {'slug':('country_name',)} 
    
    class Meta:
        model=Countries

class OperatorAdmin(admin.ModelAdmin):
    list_display = ['operator_name','slug']
    prepopulated_fields = {'slug':('operator_name',)} 
    
    class Meta:
        model=Operators
        
admin.site.register(Countries, CountryAdmin)
admin.site.register(Operators, OperatorAdmin)

