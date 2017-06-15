from rest_framework import serializers
from auctions.models import Auction, Item


class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ('id', 'name', 'auctioneer', )


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'lot', 'run', 'item_category', )


class AuctionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'lot', 'run', 'item_category', 'auction', 'auctioneer', )



