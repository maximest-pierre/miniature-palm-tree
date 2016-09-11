from django.test import TestCase
from inventory.models import Item, ItemGroup
from datetime import date

class ItemTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        item = Item.objects.create(
            name="123", creation_date=date.today, arrival_date=date.today
        )

    def testName(self):
        item = Item.objects.get(name="123")
        self.assertEqual(item.name, "123")

    def testCreationDate(self):
        item = Item.objects.get(name="123")
        self.assertEqual(item.creation_date, date.today)

    def testArrivalDate(self):
        item = Item.objects.get(name="123")
        self.assertEqual(item.arrival_date, date.today)
