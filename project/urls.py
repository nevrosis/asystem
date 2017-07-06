from django.conf.urls import url, include
from django.contrib import admin
from auctions import views
from auctions.api import urls as api_url
from django.conf import settings
from django.conf.urls.static import static


import debug_toolbar
urlpatterns = [

    url(r'^__debug__/', include(debug_toolbar.urls)),

    url(r'^auctioneer-registration-completed/$', views.AuctioneerRegistrationCompleted.as_view(), name='AuctioneerRegistrationCompleted'),
    url(r'^auctioneer-registration-form/$', views.AuctioneerRegistrationForm.as_view(), name='AuctioneerRegistrationForm'),
    url(r'^bidder-registration-form/$', views.BidderRegistrationForm.as_view(), name='BidderRegistrationForm'),

    url(r'^auctions/details/(?P<auction_id>[0-9]+)', views.catalog_auction_details, name='auction_details'),
    url(r'^auctions/', views.catalog_auctions, name='auctions'),

    url(r'^categories/', views.catalog_categories, name='categories'),

    url(r'^items/(?P<item_id>[0-9]+)/$', views.catalog_item_details, name='item'),
    url(r'^items/', views.catalog_items, name='items'),

    url(r'^search/(?P<criteria>[\w\-_%20]+)', views.catalog_search, name='search'),

    url(r'^auctioneers/(?P<auctioneer_slug>[\w\-_]+)/auctions/(?P<auction_slug>[\w\-_]+)/items/(?P<item_slug>[\w\-_]+)/$', views.catalog_auctioneers_auctions_items_details, name='catalog_auctioneers_auctions_items_details'),
    url(r'^auctioneers/(?P<auctioneer_slug>[\w\-_]+)/auctions/(?P<auction_slug>[\w\-_]+)/items/$', views.catalog_auctioneers_auctions_items, name='catalog_auctioneers_auctions_items'),
    url(r'^auctioneers/(?P<auctioneer_slug>[\w\-_]+)/auctions/$', views.catalog_auctioneers_auctions, name='catalog_auctioneers_auctions'),
    url(r'^auctioneers/(?P<auctioneer_slug>[\w\-_]+)/details/$', views.catalog_auctioneers_details, name='catalog_auctioneers_details'),
    url(r'^auctioneers/', views.catalog_auctioneers, name='auctioneers'),

    url(r'^api/', include(api_url)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^$', views.catalog_index, name='index'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
