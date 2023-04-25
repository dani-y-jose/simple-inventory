from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    Custom user admin class.
    """

    pass


admin.site.register(CustomUser, CustomUserAdmin)
