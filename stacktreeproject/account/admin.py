from django.contrib import admin
from .models import *

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm,UserChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('name','email','phone_number','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None,{'fields':('name','email','password')}),
        ("Personal info",{'fields':('phone_number',)}),
        ("Permissions",{'fields':('is_admin',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','email','phone_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

admin.site.register(User_seleceted_tree)
admin.site.register(User_mastered_language_syntax)
admin.site.register(User_mastered_framework_syntax)
admin.site.register(User_to_master_language_syntax)
admin.site.register(User_to_master_framework_syntax)
admin.site.register(Like_company)
admin.site.register(Like_job)
admin.site.register(Like_framework)
admin.site.register(Like_language)

# Register your models here.
