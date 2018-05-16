from django.db import models

# Create your models here.
class WatchMan:
    name = models.CharField(max_length = 40)
    birthday = models.DateTimeField()
    password = models.CharField(max_length = 40)
    
    class Meta:
        ordering = ("name",)
        
    def __str__(self):
        return self.name
        
 
