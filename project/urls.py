from django.conf.urls import url, include
from django.contrib import admin
from auctions import views
from auctions.api import urls as api_url

urlpatterns = [

    url(r'^auctions/details/(?P<auction_id>[0-9]+)', views.catalog_auction_details, name='auction_details'),
    # I need to slug HERE for the

    # This URL will be for listing
    #url(r'^auctions/(?P<auction_id>[0-9]+)', views.catalog_auction_items, name='auction_items'),

    # this URL will be for the ITEMS inside a specific sale
    #url(r'^auctions/(?P<auction_id>[0-9]+)/items/(?P<item_id>[0-9]+)/$', views.catalog_auction_items, name='auction_items'),

    url(r'^auctions/', views.catalog_auctions, name='auctions'),

    url(r'^items/(?P<item_id>[0-9]+)', views.catalog_item_details, name='item'),
    url(r'^items/', views.catalog_items, name='items'),

    # url(r'^auctioneers/auctions/', views.catalog_auctioneers, name='auctioneers'),
    url(r'^auctioneers/(?P<auctioneer_slug>[\w\-_]+)/auctions/$', views.catalog_auctioneers_auctions, name='catalog_auctioneers_auctions'),
    url(r'^auctioneers/(?P<auctioneer_slug>[\w\-_]+)/details/$', views.catalog_auctioneers_details, name='catalog_auctioneers_details'),

    url(r'^auctioneers/', views.catalog_auctioneers, name='auctioneers'),

    url(r'^$', views.catalog_index, name='index'),

    url(r'^api/', include(api_url)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
