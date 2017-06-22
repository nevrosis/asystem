from django.conf.urls import url

from .views import (
    auction_detail,
    item_list,
    item_detail,
    auction_list,
    auctioneer_detail,
    auctioneer_list,
    item_listing,
    auction_listing,
)

urlpatterns = [

    url(r'^auctioneers/$', auctioneer_list),
    url(r'^auctioneers/(?P<pk>[0-9]+)/$', auctioneer_detail),
    url(r'^auctions/$', auction_list),
    url(r'^auctions/(?P<pk>[0-9]+)/$', auction_detail),

    url(r'^auction_listing/(?P<auction_id>[0-9]+)/$', auction_listing),
    url(r'^item_listing/(?P<auction_id>[0-9]+)/$', item_listing),

    url(r'^items/$', item_list),
    url(r'^items/(?P<pk>[0-9]+)/$', item_detail),

]
