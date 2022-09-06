from django.db import models
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Card(BaseModel):
    health = models.IntegerField()
    attack = models.IntegerField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Deck(BaseModel):
    name = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="decks"
    )
    cards = models.ManyToManyField(Card)
