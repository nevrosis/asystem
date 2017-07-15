from django.contrib import admin
from auctions.models import (
    Auction,
    ItemCategory,
    Item,
    Auctioneer,
    ItemPicture,
    Bid,
    AuctioneerAddress,
    AuctioneerShippingAddress,
)

admin.site.site_header = 'asystem admin'


class BidAdmin(admin.ModelAdmin):
    list_display = ('amount', 'user', 'item', 'created_date',)
    fieldsets = (
        ("General", {
            'fields': ('amount', 'user', 'item', 'ip', )
        }),
        ("Cancelled", {
            'fields': ('cancelled', 'cancelled_date', 'cancelled_by_user',)
        }),
    )


class ItemPictureTabularInlineAdmin(admin.TabularInline):
    model = ItemPicture
    extra = 0


class AuctionAdmin(admin.ModelAdmin):
    list_display = ('name', 'published', 'auctioneer', 'terminated',)
    list_filter = ('auctioneer',)
    fieldsets = (
        ("General", {
            'fields': ('published',)
        }),
        ("Auction name", {
            'fields': ('name', 'auctioneer',)
        }),
        ("Auction Dates", {
            'fields': ('auction_start_date', 'auction_end_date',)
        }),
        ("Auction Descriptions", {
            'fields': ('summary', 'description',)
        }),
        ("Auction Rules", {
            'fields': ('terms_and_conditions', 'buyers_fees', 'off_site_terms_and_conditions',)
        }),
        ("Auction Status", {
            'fields': ('terminated', 'terminated_date',)
        }),
    )


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'published', 'lot', 'run', 'auctioneer', 'auction', 'item_categories_display', 'item_picture_count',)
    list_filter = ('auction', 'item_categories', 'published',)
    list_editable = ('published', 'lot', 'run',)
    inlines = [ItemPictureTabularInlineAdmin]
    fieldsets = (
        (None, {
            'fields': (('name', 'published'), ('lot', 'run'), 'auctioneer', 'auction',)
        }),
        ('Advanced options', {
            'fields': ('item_categories',)
        }),
    )

    # def get_queryset(self, request):
    #    qs = super().get_queryset(request)
    #        if request.user.is_superuser:
    #            return qs
    #    return qs.filter(user=request.user)


class AuctioneerAddressTabularInlineAdmin(admin.TabularInline):
    model = AuctioneerAddress
    extra = 0


class AuctioneerShippingAddressTabularInlineAdmin(admin.TabularInline):
    model = AuctioneerShippingAddress
    extra = 0


class AuctioneerAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'activated',)
    list_filter = ('activated',)
    list_editable = ('activated',)
    inlines = [AuctioneerAddressTabularInlineAdmin, AuctioneerShippingAddressTabularInlineAdmin]
    inlines = [AuctioneerAddressTabularInlineAdmin, AuctioneerShippingAddressTabularInlineAdmin]
    fieldsets = (
        ("General", {
            'fields': (('name', 'activated'), 'motto',)
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = (
        ("General", {
            'fields': ('name',)
        }),
    )


class ItemPictureAdmin(admin.ModelAdmin):
    list_display = ('name', 'primary', 'order', 'item',)
    # list_filter = ('item',)
    fieldsets = (
        ("General", {
            'fields': ('name', 'item', 'primary', 'order', 'picture')
        }),
    )


admin.site.register(Bid, BidAdmin)
admin.site.register(Auction, AuctionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Auctioneer, AuctioneerAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(ItemPicture, ItemPictureAdmin)
