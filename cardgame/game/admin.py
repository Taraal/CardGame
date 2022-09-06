# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import (
    MainUserChangeForm,
    MainUserCreationForm,
    CardCreationForm,
    DeckCreationForm,
)
from .models import CustomUser, Card, Deck


class CustomUserAdmin(UserAdmin):
    add_form = MainUserCreationForm
    form = MainUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
    ]


class CardAdmin(admin.ModelAdmin):
    add_form = CardCreationForm
    model = Card
    list_display = ["name", "attack", "health", "description"]


class DeckAdmin(admin.ModelAdmin):
    add_form = DeckCreationForm
    model = Deck
    list_display = ['user', 'name']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Deck, DeckAdmin)
