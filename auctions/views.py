import codecs
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View
from .forms import AuctioneerRegistration, BidderRegistration, ItemCSVUploadForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.admin.views.decorators import staff_member_required
import io


from auctions.models import (
    Auction,
    Auctioneer,
    Item,
    ItemCategory
)


@staff_member_required
def auction_item_import_csv(request, auction_id):
    auction = get_object_or_404(Auction, pk=auction_id)
    if request.method == 'POST':
        form = ItemCSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = io.StringIO(request.FILES['csv_file'].read().decode('utf-8'))
            auction.import_item_csv(file)
            return redirect('index')
    else:
        form = ItemCSVUploadForm()

    context = {
        'form': form,
    }
    return render(request, 'auction_item_import_csv_form.html', context)


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
    auctioneers = Auctioneer.objects.filter(activated=True).order_by('name')
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


def catalog_categories(request):
    item_categories = ItemCategory.objects.all().order_by('name')
    context = {
        'item_categories': item_categories,
    }
    return render(request, 'categories.html', context)


def catalog_item_details(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'item_details.html', context)


def catalog_items(request):
    items_list = Item.objects.filter(published=True).order_by('run').order_by('lot').order_by('name')

    paginator = Paginator(items_list, 3)
    page = request.GET.get('page')

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    context = {
        'items': items,
    }
    return render(request, 'items.html', context)


def catalog_search(request, criteria):
    items = Item.objects.filter(name__contains=criteria)
    context = {
        'items': items
    }
    return render(request, 'search.html', context)


def catalog_auction_items(request, auction_id, item_id):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'items.html', context)


class AuctioneerRegistrationForm(View):
    form_class = AuctioneerRegistration
    template_name = 'auctioneer_registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            auctioneer = form.save(commit=False)
            auctioneer.name = form.cleaned_data.get('name')

            try:
                auctioneer.save()
            except Exception as e:
                return render(request, self.template_name, {'form': form, 'error': 'Email Already in Use.'})

            return redirect('AuctioneerRegistrationCompleted')

        return render(request, self.template_name, {'form': form, 'error': 'Please fill this form.'})


class AuctioneerRegistrationCompleted(View):
    template_name = 'auctioneer_registration_completed.html'

    def get(self, request):
        return render(request, self.template_name)


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
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')

            # try:
            #     validate_email(email)
            #     valid_email = True
            # except validate_email.ValidationError:
            #     valid_email = False
            #
            # if not valid_email:
            #     return render(request, self.template_name, {'form': form, 'error': 'Invalid email address.'})

            user.username = email
            user.set_password(password)

            try:
                user.save()
            except Exception as e:
                return render(request, self.template_name, {'form': form, 'error': 'Email Already in Use.'})

            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form, 'Error': 'please fill this form.'})


# class BidderRegistrationForm(View):