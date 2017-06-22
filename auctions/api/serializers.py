from rest_framework import serializers
from auctions.models import Auction, Item, Auctioneer, ItemCategory


class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ('id', 'name', 'auctioneer', )


class AuctioneerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auctioneer
        fields = ('id', 'name', )


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ('id', 'name',)


class ItemSerializer(serializers.ModelSerializer):
    item_categories = ItemCategorySerializer(many=True)

    class Meta:
        model = Item
        fields = ('id', 'name', 'lot', 'run', 'item_categories', )


class ItemListingSerializer(serializers.Serializer):
    auction = AuctionSerializer()
    auctioneer = AuctioneerSerializer(source='auction.auctioneer')
    items = ItemSerializer(source='auction.items', many=True)

#    def get_items(self, obj):
#        items = obj.item_set.order_by('lot')
#        return ItemSerializer(items, many=True)

#    class Meta(AuctionSerializer.Meta):
#        fields = ('id', 'name', 'auctioneer', 'items')


#        model = Item
#        fields = ('id', 'name', 'lot', 'run', 'item_category', 'auction', 'auctioneer', )


#class AuctionSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Auction
#        fields = ('id', 'name', 'auctioneer', )


class AuctionListingSerializer(serializers.Serializer):
    auction = AuctionSerializer()
    auctioneer = AuctioneerSerializer(source='auction.auctioneer')
