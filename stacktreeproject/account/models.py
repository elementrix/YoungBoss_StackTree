from django.db import models


#유저정보
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_Password = models.CharField(max_length=45)
    user_Email = models.CharField(max_length=45)
    user_HP = models.TextField()
    user_Birthday = models.DateTimeField(auto_now=False)

    tree_id = models.ManyToManyField('main.Tree',blank=True, through="User_seleceted_tree")
    mastered_language_syntax = models.ManyToManyField('main.Language_syntax', blank=True, through="User_mastered_language_syntax",related_name='mastered_language')
    mastered_framework_syntax = models.ManyToManyField('main.Framework_syntax', blank=True, through="User_mastered_framework_syntax",related_name='mastered_framework')
    to_master_language_syntax = models.ManyToManyField('main.Language_syntax', blank=True, through="User_to_master_language_syntax")
    to_master_framework_syntax = models.ManyToManyField('main.Framework_syntax', blank=True, through="User_to_master_framework_syntax")

    company = models.ManyToManyField('main.Company',blank=True, through='Like_company')
    job = models.ManyToManyField('main.Job',blank=True, through='Like_job')
    framework = models.ManyToManyField('main.Framework',blank=True, through='Like_framework')
    language = models.ManyToManyField('main.Language',blank=True, through='Like_language')


#유저가 가지고 있는 트리
class User_seleceted_tree(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    tree_id = models.ForeignKey('main.Tree',on_delete = models.CASCADE)


#<<<<<<< HEAD
class Like(models.Model):
    User_id=models.ManytoManyField('User',blank=False)
    Company_id=models.ManytoManyField('Company',blank=True)
    Job_id=models.ManytoManyField('Job',blank=True)
    Tree_id=models.ManytoManyField('Tree',blank=True)
    Framework_id=models.ManytoManyField('Framework',blank=True)
    Language_id=models.ManytoManyField('Language',blank=True)

#=======
#유저가 마스터 한 언어 문법들
class User_mastered_language_syntax(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    language_syntax_id = models.ForeignKey('main.Language_syntax',on_delete = models.CASCADE,)
#>>>>>>> 52d9c4dbce5c898e576c459dfb711a795635d9fd


#유저가 마스터 한 프레임워크 문법들
class User_mastered_framework_syntax(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    framework_syntax_id=models.ForeignKey('main.Framework_syntax',on_delete = models.CASCADE)


#유저가 마스터 해야 하는 언어 문법들
class User_to_master_language_syntax(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    language_syntax_id = models.ForeignKey('main.Language_syntax',on_delete = models.CASCADE)

#유저가 마스터 해야 하는 프레임워크 문법들
class User_to_master_framework_syntax(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    framework_syntax_id = models.ForeignKey('main.framework_syntax',on_delete = models.CASCADE)


#유저가 좋아요 표시한 회사
class Like_company(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    company_id = models.ForeignKey('main.Company',on_delete = models.CASCADE)


#유저가 좋아요 표시한 것
class Like_job(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    job_id = models.ForeignKey('main.Job',on_delete = models.CASCADE)


#유저가 좋아요 표시한 것
class Like_framework(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    framework_id = models.ForeignKey('main.Framework',on_delete = models.CASCADE)


#유저가 좋아요 표시한 것
class Like_language(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    language_id = models.ForeignKey('main.Language',on_delete = models.CASCADE)