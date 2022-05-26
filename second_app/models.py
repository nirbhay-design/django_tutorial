from django.db import models

# Create your models here.
# class Second_app:
#     id = 0
#     def __init__(self,name,email,phno):
#         self.name = name
#         self.email = email
#         self.phno = phno
#         Second_app.id += 1
#         self.id = Second_app.id

class Second_app(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    phno = models.CharField(max_length=15)
