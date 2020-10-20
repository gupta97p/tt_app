from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import user_reg


admin.site.register(user_reg, UserAdmin)
