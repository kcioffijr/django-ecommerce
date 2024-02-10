from django.test import Client, TestCase
from django.urls import reverse


class TestCheckoutView(TestCase):
    def setUp(self):
        self.client = Client()
        self.form_data = {"first_name": "Michael",
                            "last_name": "Dillon",
                            "email": "donald74@hotmail.com",
                            "phone_number": "875-844-6600",
                            "street": "7762 Newman Flats Suite 388",
                            "zip": "24306",
                            "city": "New Cindychester",
                            "state": "Pennsylvania"}

    def test_form_display(self):
        response = self.client.get(reverse('store:checkout'))
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form)
        