from django.db import models

class Message(models.Model) :
    name = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    title = models.CharField(max_length=150,null=True,blank=True)
    text = models.TextField()
    
    def __str__(self):
        return self.email