from django.db import models


#언어정보
class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    language_name = models.CharField(max_length=45)
    language_description = models.TextField()


#언어에 대한 문법 정보
class Language_syntax(models.Model):
    language_syntax_id = models.AutoField(primary_key=True)
    l_syntax_title = models.CharField(max_length=45)
    l_syntax_difficulty = models.IntegerField()
    language_id = models.ForeignKey('Language',on_delete = models.CASCADE)
    l_syntax_teer = models.CharField(max_length=45)
    l_syntax_order = models.IntegerField()


#프레임워크 정보
class Framework(models.Model):
    framework_id = models.AutoField(primary_key=True)
    framework_name = models.CharField(max_length=45)
    framework_description = models.TextField()

    language = models.ManyToManyField('Language',blank = True,through = 'Language_to_master_framework')
    syntax = models.ManyToManyField('Language_syntax', blank = True, through = 'Syntax_to_master_framework')

#프레임워크에 대한 문법 정보
class Framework_syntax(models.Model):
    framework_syntax_id = models.AutoField(primary_key=True)
    f_syntax_title = models.CharField(max_length=45)
    f_syntax_difficulty = models.IntegerField()
    framework_id = models.ForeignKey('Framework',on_delete = models.CASCADE)
    f_syntax_teer = models.CharField(max_length=45)
    f_syntax_order = models.IntegerField()


#선수언어
class Language_to_master_framework(models.Model):
    language_id = models.ForeignKey('Language',on_delete = models.CASCADE)
    framework_id = models.ForeignKey('Framework',on_delete = models.CASCADE)


"""
프레임워크를 배운다고 해도, 선수언어의 모든 문법을 마스터 할 필요는 없기 때문에
마스터 해야 하는 문법만을 표시
"""
class Syntax_to_master_framework(models.Model):
    language_syntax_id = models.ForeignKey('Language_syntax',on_delete = models.CASCADE)
    framework_id = models.ForeignKey('Framework',on_delete = models.CASCADE)


#회사정보
class Company(models.Model):
    Company_id = models.AutoField(primary_key=True)
    Company_name = models.CharField(max_length=45)
    Company_Address = models.TextField()
    # (추후추가) Field_id=models.ForeignKey('Field')
    Company_description=models.TextField()


#트리정보 : Tree_name 은 포지션으로 일단은 확정
class Tree(models.Model):
    Tree_id = models.AutoField(primary_key=True)
    Tree_name = models.CharField(max_length=45)

    framework = models.ManyToManyField('Framework', blank=True, through='Framework_for_tree')
    language = models.ManyToManyField('Language', blank=True, through='Language_for_tree')


#직무정보
class Job(models.Model):
    Job_id=models.AutoField(primary_key=True)
    Job_name=models.CharField(max_length=45)
    Tree_id=models.ForeignKey('Tree', on_delete=models.CASCADE)
    # (추후추가) Field_id=models.ForeignKey('Field')
    Company_id=models.ForeignKey('Company', on_delete=models.CASCADE)


"""
직무카테고리 (소셜네트워크, OTT등등 나중에 추가)
"""
# class Field(models.Model):
#     Field_id=models.AutoField(primary_key=True)
#     Field_name=models.CharField(max_length=45)


#트리에 달려있는 프레임워크
class Framework_for_tree(models.Model):
     framework_id = models.ForeignKey('Framework',on_delete = models.CASCADE)
     tree_id = models.ForeignKey('Tree',on_delete = models.CASCADE)

     order = models.IntegerField(null=False)
     essential = models.BooleanField(default=True)
     choice = models.IntegerField(null=True)


#트리에 달려있는 언어
class Language_for_tree(models.Model):
     language_id = models.ForeignKey('Language',on_delete = models.CASCADE)
     tree_id = models.ForeignKey('Tree',on_delete = models.CASCADE)

     order = models.IntegerField(null=False)
     essential = models.BooleanField(default=True)
     choice = models.IntegerField(null=True)
