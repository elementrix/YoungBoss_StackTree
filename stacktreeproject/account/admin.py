from django.contrib import admin
from .models import *

admin.site.register(User)
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
