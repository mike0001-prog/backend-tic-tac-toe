from django.db import models

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    list = models.ForeignKey(List,on_delete=models.CASCADE,null=True)
    text  = models.CharField(max_length=20)

    def __str__(self):
        return f"#{self.text} "
    
# class Room(models.Model):
#     """
#     Represents a chat room where users can communicate
#     """
#     name = models.CharField(max_length=255, unique=True)
#     slug = models.SlugField(unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         ordering = ['-created_at']
    
#     def __str__(self):
#         return self.name


    