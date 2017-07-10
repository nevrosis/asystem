from django.db import models
from django.db.models import CharField, TextField, BooleanField, IntegerField, SlugField, ImageField
# from django.db.models.signals import pre_save
# from django.utils.text import slugify
# from uuslug import slugify
from uuslug import uuslug
import csv


class Auction(models.Model):
    name = CharField(max_length=255, verbose_name='Name')
    slug = SlugField(max_length=255, unique=True, db_index=True)
    summary = CharField(max_length=512, blank=True, null=True, verbose_name='Summary')
    description = TextField(blank=True, null=True, verbose_name='Description')
    terms_and_conditions = TextField(blank=True, null=True, verbose_name='Terms and Conditions')
    buyers_fees = TextField(blank=True, null=True, verbose_name="Buyer's fees")
    off_site_terms_and_conditions = TextField(blank=True, null=True, verbose_name='Off Site terms and conditions')
    published = models.BooleanField(default=False, verbose_name='Published')
    auction_start_date = models.DateTimeField(blank=True, null=True, verbose_name='Auction start date')
    auction_end_date = models.DateTimeField(blank=True, null=True, verbose_name='Auction end date')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    auctioneer = models.ForeignKey("Auctioneer", on_delete=models.CASCADE, verbose_name='Auctioneer',
                                   related_name="auctions")
    terminated = models.BooleanField(default=False, verbose_name='Terminated')
    terminated_date = models.DateTimeField(blank=True, null=True, verbose_name='Date terminated')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Auction, self).save(*args, **kwargs)

    def import_item_csv(self, file_data):
        reader = csv.DictReader(file_data)

        for item in reader:
            obj, created = Item.objects.update_or_create(lot=item['lot'], auction=self, defaults={
                'name': item['name'],
                'description': item['description'],
                'auctioneer': self.auctioneer
            })

    class Meta:
        ordering = ('name',)


class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    item = models.ForeignKey("Item", on_delete=models.CASCADE, verbose_name='Item')
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, verbose_name='User')
    cancelled = models.BooleanField(default=False)
    cancelled_date = models.DateTimeField(blank=True, null=True)
    cancelled_by_user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="cancelled_by_user",
                                          blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Item(models.Model):
    name = CharField(max_length=512, verbose_name='Name')
    slug = SlugField(max_length=512, unique=True, db_index=True)
    lot = CharField(max_length=25, verbose_name='Lot Number')
    run = CharField(max_length=25, verbose_name='Run Number')
    description = TextField(blank=True, null=True, verbose_name='Description')
    published = models.BooleanField(default=False, verbose_name='Published')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    auctioneer = models.ForeignKey("Auctioneer", on_delete=models.CASCADE, verbose_name='Auctioneer')
    auction = models.ForeignKey("Auction", on_delete=models.CASCADE, blank=True, null=True, verbose_name='Auction',
                                related_name="items")
    item_categories = models.ManyToManyField("ItemCategory", related_name="items")

    def item_categories_display(self):
        display_list = list(self.item_categories.all().order_by('name'))
        return display_list

    item_categories_display.short_description = 'Categories'

    def item_categories_query(self):
        display_query_set = self.item_categories.all().order_by('name')
        return display_query_set

    def item_picture_count(self):
        pic_count = self.item_pictures.all().count()
        return pic_count

    item_picture_count.short_description = 'Pic'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Item, self).save(*args, **kwargs)

    class Meta:
        ordering = ('lot', 'run', 'name')


class Auctioneer(models.Model):
    name = CharField(max_length=255, verbose_name='Name', unique=True)
    slug = SlugField(max_length=255, unique=True, db_index=True)
    motto = CharField(max_length=255, blank=True, null=True)
    activated = models.BooleanField(default=False, verbose_name='Activated')
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

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(Auctioneer, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)


class ItemCategory(models.Model):
    name = CharField(max_length=64, verbose_name='Name')
    slug = SlugField(max_length=64, unique=True, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.name, instance=self)
        super(ItemCategory, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)


#
# def pre_save_item_signal_receiver(sender, instance, *args, **kwargs):
#    slug = slugify(instance.name)
#    exists = Item.objects.filter(slug=slug).exists()
#    if exists:
#        slug = "%s-%s" %(slug, instance.id)
#    instance.slug = slug
#
# pre_save.connect(pre_save_item_signal_receiver, sender=Item)


class ItemPicture(models.Model):
    name = CharField(max_length=256, verbose_name='Name', blank=True, null=True, default=" ")
    primary = BooleanField(default=False)
    order = IntegerField(default=0)
    picture = ImageField(blank=True, null=True, verbose_name='Picture')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    item = models.ForeignKey("Item", on_delete=models.CASCADE, blank=True, null=True, verbose_name='Item',
                             related_name="item_pictures")

    # def __str__(self):
    #     return self.name
    def test(self):
        return "test"

    class Meta:
        ordering = ('-primary', 'order')
