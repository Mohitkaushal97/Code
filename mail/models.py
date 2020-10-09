from django.db import models

# Create your models here.


class FormM(models.Model):
   
    email = models.EmailField()
    Subject= models.CharField(max_length=50)
    Message = models.CharField(max_length=50)


    def __str__(self):
        return self.email + '-' + str(self.id)