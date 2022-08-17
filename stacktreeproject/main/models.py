from django.db import models

# Create your models here.
class Language(models.Model):
    Language_id=models.AutoField(primary_key=True)
    Language_name=models.CharField(max_length=45)
    Language_description=models.TextField

class LanguageSyntax(models.Model):
    LanguageSyntax_id=models.AutoField(primary_key=True)
    LSyntax_title=models.CharField(max_length=45)
    LSyntax_difficulty=models.IntegerField
    # Language_id=OnetoManyField('Language',blank=False)
    Language_id=models.ForeignKey('Language',on_delete=models.CASCADE)
    LSyntax_teer=models.CharField(max_length=45)
    LSyntax_order=models.IntegerField

class Framework(models.Model):
    Framework_id=models.AutoField(primary_key=True)
    Framework_name=models.CharField(max_length=45)
    Framework_description=models.TextField

class FrameworkSyntax(models.Model):
    FrameworkSyntax_id=models.AutoField(primary_key=True)
    FSyntax_title=models.CharField(max_length=45)
    FSyntax_difficulty=models.IntegerField
    # Language_id=OnetoManyField('Language',blank=False)
    Framework_id=models.ForeignKey('Framework',on_delete=models.CASCADE)
    FSyntax_teer=models.CharField(max_length=45)
    FSyntax_order=models.IntegerField 

class Company(models.Model):
    Company_name=models.CharField(max_length=45)
    Company_adress=models.TextField
    Field_id=models.ForeignKey('Field',on_delete=models.CASCADE)
    Company_description=models.TextField

class Tree(models.Model):
    Tree_id=models.AutoField(primary_key=True)