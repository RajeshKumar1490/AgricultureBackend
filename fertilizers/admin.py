from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from fertilizers.models import User, FarmerRequest

admin.site.register(User, UserAdmin)
admin.site.register(FarmerRequest)
