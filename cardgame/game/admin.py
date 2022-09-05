# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MainUserChangeForm, MainUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = MainUserCreationForm
    form = MainUserChangeForm
    model = CustomUser
    list_display = ["email", "username", ]


admin.site.register(CustomUser, CustomUserAdmin)
