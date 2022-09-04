from django.test import TestCase, Client
from django.urls import reverse
from App_Shop.models import Category, Product

class CategoryTest(TestCase):
    def test__str__(self):
        category=Category(title="Gift Box")
        self.assertEqual(category.__str__(),"Gift Box")

class ProductTest(TestCase):
    def test__str__(self):
        category=Category(title="Papercrafts")
        category.save()
        item = Product(name="Gift Box", price=20.0, category = category)
        item.save()
        self.assertEqual(item.__str__(),"Gift Box")