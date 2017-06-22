from django.shortcuts import render, get_object_or_404

# Create your views here.
from auctions.models import(
    Auction,
    Auctioneer,
    Item,
    ItemCategory
)


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


def catalog_auction_details(request, auction_id):
    auctions = Item.objects.all()
    context = {
        'auctions': auctions,
    }
    return render(request, 'auction_details.html', context)


def catalog_auctioneers(request):
    auctioneers = Auctioneer.objects.all()
    context = {
        'auctioneers': auctioneers,
    }
    return render(request, 'auctioneers.html', context)


def catalog_auctioneers_details(request, auctioneer_slug):
    auctioneer = get_object_or_404(Auctioneer, slug=auctioneer_slug)
    context = {
        'auctioneer': auctioneer,
    }
    return render(request, 'auctioneer_details.html', context)


def catalog_auctioneers_auctions(request, auctioneer_slug):
    auctioneer = get_object_or_404(Auctioneer, slug=auctioneer_slug)
    auctions = auctioneer.auctions.all()
    context = {
        'auctioneer': auctioneer,
        'auctions': auctions,
    }
    return render(request, 'auctioneer_auctions.html', context)


def catalog_item_details(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'item_details.html', context)


def catalog_items(request):
    items = Item.objects.all()
    item_categories = ItemCategory.objects.all().order_by('name')
    context = {
        'items': items,
        'item_categories': item_categories
    }
    return render(request, 'items.html', context)


def catalog_auction_items(request, auction_id, item_id):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'items.html', context)




