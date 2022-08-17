from email.policy import default
from xmlrpc.client import Boolean
from django.db import models


# Create your models here.

class User(models.Model):
    User_id=models.AutoField(primary_key=True)
    Tree_id=models.ManytoManyField('Tree',blank=True)
    User_Password=models.CharField(max_length=45)
    User_Email=models.CharField(max_length=45)
    User_HP=models.TextField()
    User_Birthday=models.DateTimeField(auto_now=False)



class User_mastered_syntax(models.Model):
    User_id=models.ManytoManyField('User',blank=False)
    Framework_Syntax_id=models.ManytoManyField('Framework_Syntax',blank=True)
    Language_Syntax_id=models.ManytoManyField('Language_Syntax',blank=True)

class User_to_master_syntax(models.Model):
    User_id=models.ManytoManyField('User',blank=False)
    Framework_Syntax_id=models.ManytoManyField('Framework_Syntax',blank=True)
    Language_Syntax_id=models.ManytoManyField('Language_Syntax',blank=True)


class Like(models.Model):
    User_id=models.ManytoManyField('User',blank=False)
    Company_id=models.ManytoManyField('Company',blank=True)
    Job_id=models.ManytoManyField('Job',blank=True)
    Tree_id=models.ManytoManyField('Tree',blank=True)
    Framework_id=models.ManytoManyField('Framework',blank=True)
    Language_id=models.ManytoManyField('Language',blank=True)

class Framework_for_tree(models.Model):
     Framework_id=models.ManytoManyField('Framework',blank=True)
     Tree_id=models.ManytoManyField('Tree',blank=True)
     order=models.IntegerField(null=False)
     essential=models.BooleanField(default=True)

class Language_for_tree(models.Model):
     Language_id=models.ManytoManyField('Language',blank=True)
     Tree_id=models.ManytoManyField('Tree',blank=True)
     order=models.IntegerField(null=False)
     essential=models.BooleanField(default=True)


