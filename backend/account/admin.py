from django.contrib import admin
from .models import User
from .useradmin import UserAdmin

# Register your models here.


admin.site.register(User, UserAdmin)