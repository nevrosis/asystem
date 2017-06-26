from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View
from .bidder_registration_form import BidderRegistration

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


def catalog_auctioneers_auctions_items(request, auctioneer_slug, auction_slug):
    auctioneer = get_object_or_404(Auctioneer, slug=auctioneer_slug)
    auction = get_object_or_404(Auction, slug=auction_slug)
    items = Item.objects.filter(auction_id=auction.id)
    item_categories = ItemCategory.objects.all().order_by('name')
    context = {
        'auctioneer': auctioneer,
        'auction': auction,
        'items': items,
        'item_categories': item_categories,
    }
    return render(request, 'auction_items.html', context)


def catalog_auctioneers_auctions_items_details(request, auctioneer_slug, auction_slug, item_slug):
    auctioneer = get_object_or_404(Auctioneer, slug=auctioneer_slug)
    auction = auctioneer.auctions.filter(slug=auction_slug)
    item = get_object_or_404(Item, slug=item_slug)
    item_categories = ItemCategory.objects.all().order_by('name')
    context = {
        'auctioneer': auctioneer,
        'auction': auction,
        'item': item,
        'item_categories': item_categories,
    }
    return render(request, 'item_details.html', context)


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


class BidderRegistrationForm(View):
    form_class = BidderRegistration
    template_name = 'bidder_registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})
