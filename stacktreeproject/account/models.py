from django.db import models

# Create your models here.
class User(models.Model):
    User_id=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=45)
    Tree_id=ManytoManyField('Tree',blank=True)
    User_Password=models.CharField(max_length=45)
    User_Email=models.CharField(max_length=45)
    User_HP=models.TextField()
