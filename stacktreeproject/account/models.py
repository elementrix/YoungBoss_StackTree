from email.policy import default
from xmlrpc.client import Boolean
from django.db import models


# Create your models here.

class User_mastered_syntax(models.Model):
    User_id=ManytoManyField('User',blank=False)
    Framework_Syntax_id=ManytoManyField('Framework_Syntax',blank=True)
    Language_Syntax_id=ManytoManyField('Language_Syntax',blank=True)

class User_to_master_syntax(models.Model):
    User_id=ManytoManyField('User',blank=False)
    Framework_Syntax_id=ManytoManyField('Framework_Syntax',blank=True)
    Language_Syntax_id=ManytoManyField('Language_Syntax',blank=True)


class Like(models.Model):
    User_id=ManytoManyField('User',blank=False)
    Company_id=ManytoManyField('Company',blank=True)
    Job_id=ManytoManyField('Job',blank=True)
    Tree_id=ManytoManyField('Tree',blank=True)
    Framework_id=ManytoManyField('Framework',blank=True)
    Language_id=ManytoManyField('Language',blank=True)

class Framework_for_tree(models.Model):
     Framework_id=ManytoManyField('Framework',blank=True)
     Tree_id=ManytoManyField('Tree',blank=True)
     order=IntegerField(null=False)
     essential=BooleanField(default=True)

class Language_for_tree(models.Model):
     Language_id=ManytoManyField('Language',blank=True)
     Tree_id=ManytoManyField('Tree',blank=True)
     order=IntegerField(null=False)
     essential=BooleanField(default=True)

class Job(models.Model):
    Job_id=models.AutoField(primary_key=True)
    Job_name=models.CharField(max_length=45)
    Tree_id=models.ForeignKey(Tree, on_delete=models.CASCADE)
    Field_id=models.ForeignKey(Field, on_delete=models.CASCADE)
    Company_id=models.ForeignKey(Company, on_delete=models.CASCADE)

class Field(models.Model):
    Field_id=models.AutoField(primary_key=True)
    Field_name=models.CharField(max_length=45)

class Company(models.Model):
    Company_id=models.AutoField(primary_key=True)
    Company_name=models.CharField(max_length=45)
    Company_Address=models.TextField()
    Field_id=models.ForeignKey(Field, on_delete=models.CASCADE)
    Company_description=models.TextField()

