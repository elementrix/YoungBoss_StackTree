from django.db import models

# Create your models here.

#유저정보
class User(models.Model):
    User_id=models.AutoField(primary_key=True)
    Tree_id=models.ManyToManyField('main.Tree',blank=True)
    User_Password=models.CharField(max_length=45)
    User_Email=models.CharField(max_length=45)
    User_HP=models.TextField()
    User_Birthday=models.DateTimeField(auto_now=False)


#유저가 마스터 한 문법들
class User_mastered_syntax(models.Model):
    User_id=models.ManyToManyField('User',blank=False)
    Framework_Syntax_id=models.ManyToManyField('main.Framework_syntax',blank=True)
    Language_Syntax_id=models.ManyToManyField('main.Language_syntax',blank=True)


class User_to_master_syntax(models.Model):
    User_id=models.ManyToManyField('User',blank=False)
    Framework_Syntax_id=models.ManyToManyField('main.Framework_syntax',blank=True)
    Language_Syntax_id=models.ManyToManyField('main.Language_syntax',blank=True)


class Like(models.Model):
    User_id=models.ManyToManyField('User',blank=False)
    Company_id=models.ManyToManyField('main.Company',blank=True)
    Job_id=models.ManyToManyField('main.Job',blank=True)
    Tree_id=models.ManyToManyField('main.Tree',blank=True)
    Framework_id=models.ManyToManyField('main.Framework',blank=True)
    Language_id=models.ManyToManyField('main.Language',blank=True)


class Framework_for_tree(models.Model):
     Framework_id=models.ManyToManyField('main.Framework',blank=True)
     Tree_id=models.ManyToManyField('main.Tree',blank=True)
     order=models.IntegerField(null=False)
     essential=models.BooleanField(default=True)


class Language_for_tree(models.Model):
     Language_id=models.ManyToManyField('main.Language',blank=True)
     Tree_id=models.ManyToManyField('main.Tree',blank=True)
     order=models.IntegerField(null=False)
     essential=models.BooleanField(default=True)

