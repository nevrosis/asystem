from django.contrib import admin
from auctions.models import Auction
from auctions.models import ItemCategory
from auctions.models import Item
from auctions.models import Auctioneer


class AuctionAdmin(admin.ModelAdmin):
    list_display = ('name', 'published', 'auctioneer', 'terminated',)
    list_filter = ('auctioneer', )
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
    list_display = ('name', 'published', 'lot', 'run', 'auctioneer', 'auction', 'item_categories_display', 'slug',)
    list_filter = ('auction', 'item_categories', 'published',)
    fieldsets = (
        (None, {
            'fields': (('name', 'published'), ('lot', 'run'), 'auctioneer', 'auction',)
        }),
        ('Advanced options', {
            'fields': ('item_categories',)
        }),
    )

    #def get_queryset(self, request):
    #    qs = super().get_queryset(request)
    #        if request.user.is_superuser:
    #            return qs
    #    return qs.filter(user=request.user)


class AuctioneerAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'activated', )
    list_filter = ('activated', )
    fieldsets = (
        ("General", {
            'fields': (('name', 'activated'), 'motto')
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    fieldsets = (
        ("General", {
            'fields': ('name',)
        }),
    )


admin.site.register(Auction, AuctionAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Auctioneer, AuctioneerAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
