from django.test import TestCase
from auctions.models import (
    Auctioneer,
    Auction,
)


class AuctioneerTestCase(TestCase):
    # def setUp(self):
        # print("setUp")
        # auctioneer = Auctioneer.objects.create(name="Auctioneer A")
        # print("auctioneer.id = " + str(auctioneer.id))
        # auction = Auction.objects.create(name="Auction 1 from Auctioneer A", auctioneer_id=auctioneer.id)
        # print("auction.id = " + str(auction.id))

    def test_auctioneer_creation(self):
        auctioneer = Auctioneer.objects.create(name="Auctioneer A")
        auctioneer = Auctioneer.objects.get(name="Auctioneer A")
        self.assertEqual(1, auctioneer.id)
        self.assertEqual("Auctioneer A", auctioneer.name)
        auctioneer = Auctioneer.objects.get(id=1)
        self.assertEqual(1, auctioneer.id)
        self.assertEqual("Auctioneer A", auctioneer.name)


class AuctionTestCase(TestCase):

    def test_auction_creation(self):
        auction = Auction.objects.create(name="Auction 1 from Auctioneer A", auctioneer_id=1)
        self.assertEqual(1, auction.id)
        self.assertEqual("Auction 1 from Auctioneer A", auction.name)
        auction = Auction.objects.get(id=1)
        self.assertEqual(1, auction.id)
        self.assertEqual("Auction 1 from Auctioneer A", auction.name)


