from django.db import models
from django.db.models import CharField, TextField, BooleanField, IntegerField


class Auction(models.Model):
    name = CharField(max_length=255, verbose_name='Name')
    published = models.BooleanField(default=False, verbose_name='Published')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    auctioneer = models.ForeignKey("Auctioneer", on_delete=models.CASCADE, verbose_name='Auctioneer')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Item(models.Model):
    name = CharField(max_length=512, verbose_name='Name')
    lot = CharField(max_length=25, verbose_name='Lot Number')
    run = CharField(max_length=25, verbose_name='Run Number')
    published = models.BooleanField(default=False, verbose_name='Published')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    auctioneer = models.ForeignKey("Auctioneer", on_delete=models.CASCADE, verbose_name='Auctioneer')
    auction = models.ForeignKey("Auction", on_delete=models.CASCADE, blank=True, null=True, verbose_name='Auction')
    item_category = models.ManyToManyField("ItemCategory")

    def item_category_display(self):
        display_list = list(self.item_category.all())
        return display_list

    item_category_display.short_description = 'Categories'

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Auctioneer(models.Model):
    name = CharField(max_length=255, verbose_name='Name')
    active = models.BooleanField(default=False, verbose_name='Active')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
#    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='User')
#    user = models.ManyToManyField(User)

#    def user_display(self):
#        display_list = list(self.user.all())
#        return display_list

#    user_display.short_description = 'Users'

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class ItemCategory(models.Model):
    name = CharField(max_length=64, verbose_name='Name')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)



