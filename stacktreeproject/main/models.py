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

class Language_to_master_Framework(models.Model):
    Language_id=models.ManyToManyField('Language',on_delete=models.CASCADE)
    Framework_id=models.ManyToManyField('Framework',on_delete=models.CASCADE)

class Syntax_to_master_Framework(models.Model):
    Language_Syntax_id=models.ManyToManyField('LanguageSyntax',on_delete=models.CASCADE)
    Framework_id=models.ManyToManyField('Framework',on_delete=models.CASCADE)


class Company(models.Model):
    Company_id=models.AutoField(primary_key=True)
    Company_name=models.CharField(max_length=45)
    Company_Address=models.TextField()
    Field_id=models.ForeignKey('Field', on_delete=models.CASCADE)
    Company_description=models.TextField()


class Tree(models.Model):
    Tree_id=models.AutoField(primary_key=True)

class Job(models.Model):
    Job_id=models.AutoField(primary_key=True)
    Job_name=models.CharField(max_length=45)
    Tree_id=models.ForeignKey(Tree, on_delete=models.CASCADE)
    Field_id=models.ForeignKey('Field', on_delete=models.CASCADE)
    Company_id=models.ForeignKey(Company, on_delete=models.CASCADE)

class Field(models.Model):
    Field_id=models.AutoField(primary_key=True)
    Field_name=models.CharField(max_length=45)

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
