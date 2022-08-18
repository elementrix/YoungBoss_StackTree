from django.contrib import admin
from .models import *

admin.site.register(Language)
admin.site.register(Language_syntax)
admin.site.register(Framework)
admin.site.register(Framework_syntax)
admin.site.register(Syntax_to_master_framework)
admin.site.register(Company)
admin.site.register(Tree)
admin.site.register(Framework_for_tree)
admin.site.register(Language_for_tree)

# Register your models here.
