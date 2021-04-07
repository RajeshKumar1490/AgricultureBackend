from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from fertilizers.models import User

admin.site.register(User, UserAdmin)
