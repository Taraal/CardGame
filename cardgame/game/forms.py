from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Card, Deck


class MainUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username",)


class MainUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username",)


class CardCreationForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'


class DeckCreationForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = "__all__"
