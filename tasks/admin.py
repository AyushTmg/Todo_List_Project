from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
        list_display=['fullname','username','email']
        list_per_page=10
        search_fields=['fullname']

        add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name","last_name","email","username", "password1", "password2"),
            },
        ),
    )
        def fullname(self,user):
                return f"{user.first_name} {user.last_name}"
        
@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
        list_display=["title",'description',"status","date","complete"]
        list_editable=['status']
        list_per_page=10
        search_fields=['title']
        autocomplete_fields=['user']

        



