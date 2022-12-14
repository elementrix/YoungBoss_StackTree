from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, name, real_name, email, password=None):
        if not name:
            raise ValueError('must have user email')
        if not email:
            raise ValueError('must have user email')
        user = self.model(
            name=name,
            real_name=real_name,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, real_name, email, password):
        user = self.create_user(
            name=name,
            real_name=real_name,
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=255,unique=True)
    real_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    tree_id = models.ManyToManyField('main.Tree',blank=True, through="User_seleceted_tree")
    mastered_language_syntax = models.ManyToManyField('main.Language_syntax', blank=True, through="User_mastered_language_syntax",related_name='mastered_language')
    mastered_framework_syntax = models.ManyToManyField('main.Framework_syntax', blank=True, through="User_mastered_framework_syntax",related_name='mastered_framework')
    to_master_language_syntax = models.ManyToManyField('main.Language_syntax', blank=True, through="User_to_master_language_syntax")
    to_master_framework_syntax = models.ManyToManyField('main.Framework_syntax', blank=True, through="User_to_master_framework_syntax")

    company = models.ManyToManyField('main.Company',blank=True, through='Like_company')
    job = models.ManyToManyField('main.Job',blank=True, through='Like_job')
    framework = models.ManyToManyField('main.Framework',blank=True, through='Like_framework')
    language = models.ManyToManyField('main.Language',blank=True, through='Like_language')

    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email','real_name',]
    
    def __str__(self):
        return self.name
        
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


#????????? ????????? ?????? ??????
class User_seleceted_tree(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    tree_id = models.ForeignKey('main.Tree',on_delete = models.CASCADE)

#????????? ????????? ??? ?????? ?????????
class User_mastered_language_syntax(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    language_syntax_id = models.ForeignKey('main.Language_syntax',on_delete = models.CASCADE,)

#????????? ????????? ??? ??????????????? ?????????
class User_mastered_framework_syntax(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    framework_syntax_id=models.ForeignKey('main.Framework_syntax',on_delete = models.CASCADE)


#????????? ????????? ?????? ?????? ?????? ?????????
class User_to_master_language_syntax(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    language_syntax_id = models.ForeignKey('main.Language_syntax',on_delete = models.CASCADE)

#????????? ????????? ?????? ?????? ??????????????? ?????????
class User_to_master_framework_syntax(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    framework_syntax_id = models.ForeignKey('main.framework_syntax',on_delete = models.CASCADE)


#????????? ????????? ????????? ??????
class Like_company(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    company_id = models.ForeignKey('main.Company',on_delete = models.CASCADE)


#????????? ????????? ????????? ???
class Like_job(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    job_id = models.ForeignKey('main.Job',on_delete = models.CASCADE)


#????????? ????????? ????????? ???
class Like_framework(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    framework_id = models.ForeignKey('main.Framework',on_delete = models.CASCADE)


#????????? ????????? ????????? ???
class Like_language(models.Model):
    user_id = models.ForeignKey('User',on_delete = models.CASCADE)
    language_id = models.ForeignKey('main.Language',on_delete = models.CASCADE)