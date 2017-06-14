from django.db import models
from django.contrib.auth.models import AbstractUser
from auctions.models import Auctioneer


class User(AbstractUser):
    note = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    auctioneer = models.ForeignKey(Auctioneer, on_delete=models.CASCADE, blank=True, null=True)
