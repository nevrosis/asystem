from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from auctions.serializers import(
    AuctionSerializer,
    ItemSerializer,
    ItemListingSerializer,
    AuctioneerSerializer,
    AuctionListingSerializer,
)
from auctions.models import(
    Auction,
    Item,
    Auctioneer,
    ItemCategory
)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def auction_list(request, format=None):
    if request.method == 'GET':
        auction = Auction.objects.all()
        serializer = AuctionSerializer(auction, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuctionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def auction_detail(request, pk, format=None):

    try:
        auction = Auction.objects.get(pk=pk)
    except Auction.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = AuctionSerializer(auction)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AuctionSerializer(auction, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        auction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def auctioneer_list(request, format=None):
    if request.method == 'GET':
        auctioneer = Auctioneer.objects.all()
        serializer = AuctioneerSerializer(auctioneer, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuctioneerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def auctioneer_detail(request, pk, format=None):

    try:
        auctioneer = Auctioneer.objects.get(pk=pk)
    except Auctioneer.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = AuctioneerSerializer(auctioneer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AuctioneerSerializer(auctioneer, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        auctioneer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def item_list(request, format=None):
    if request.method == 'GET':
        item = Item.objects.all()
        serializer = ItemSerializer(item, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def item_detail(request, pk, format=None):

    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def item_listing(request, auction_id):
    if request.method == 'GET':
        auction = Auction.objects.get(id=auction_id)
        serializer = ItemListingSerializer({"auction": auction})
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def auction_listing(request, auction_id):
    if request.method == 'GET':
        auction = Auction.objects.get(id=auction_id)
        serializer = AuctionListingSerializer({"auction": auction})
        return Response(serializer.data)


def catalog_index(request):
    context = {
        'show_carousel': True,
    }
    return render(request, 'index.html', context)


def catalog_auctions(request):
    auctions = Auction.objects.all()
    context = {
        'auctions': auctions,
    }
    return render(request, 'auctions.html', context)


def catalog_auctioneer(request):
    return render(request, 'auctioneer.html')


def catalog_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'item.html', context)


def catalog_items(request):
    items = Item.objects.all()
    item_categories = ItemCategory.objects.all().order_by('name')
    context = {
        'items': items,
        'item_categories': item_categories
    }
    return render(request, 'items.html', context)


def catalog_auction_items(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'items.html', context)



