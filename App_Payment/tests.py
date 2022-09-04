from django.test import TestCase
from django.urls import reverse
from App_Payment.models import BillingAddress
from App_Login.models import User, Profile
from App_Payment.forms import BillingForm


# Create your tests here.


#Testing models classes
class BillingAddressTest(TestCase):
    def setUp(self) -> None:
        user = User(email="anika@gmail.com")
        user.save()
        profile = Profile(username="Anika")
        self.billingAddress=BillingAddress(user=user)
        self.billingAddress.user.profile=profile

    def test__str__(self):
        self.assertEqual(self.billingAddress.__str__(), "Anika's billing address")

    def test_is_fully_filled(self):
        self.assertIs(self.billingAddress.is_fully_filled(),False)


class BillingFormTests(TestCase):
    def test_meta_class(self):
        form = BillingForm(data={})
        self.assertTrue(form.is_valid())


class ViewsTest(TestCase):
    def test_checkout(self):
        response = self.client.get(reverse('App_Payment:checkout'))
        self.assertEqual(response.status_code, 302)

    def test_purchase(self):
        response = self.client.get(reverse('App_Shop:home'))
        self.assertEqual(response.status_code, 200)

    def test_order_view(self):
        response = self.client.get(reverse('App_Shop:home'))
        self.assertEqual(response.status_code, 200)
