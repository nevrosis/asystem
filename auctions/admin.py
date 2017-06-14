from django.contrib import admin
from auctions.models import Auction
from auctions.models import ItemCategory
from auctions.models import Item
from auctions.models import Auctioneer


class AuctionAdmin(admin.ModelAdmin):
    list_display = ('name', 'published', 'auctioneer',)
    list_filter = ('auctioneer', )
    fieldsets = (
        ("General", {
            'fields': (('name', 'published'), 'auctioneer',)
        }),
    )


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'published', 'auctioneer', 'auction', 'item_category_display',)
    list_filter = ('auction', 'item_category', 'published',)
    fieldsets = (
        (None, {
            'fields': (('name', 'published'), 'auctioneer', 'auction',)
        }),
        ('Advanced options', {
            'fields': ('item_category',)
        }),
    )


class AuctioneerAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'active', )
    list_filter = ('active', )
    fieldsets = (
        ("General", {
            'fields': (('name', 'active'), )
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
#        if request.user.is_superuser:
#            return qs
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
