import json

from django.test import TestCase, Client
from django.urls import reverse
from .models import Customer, Plan


class CustomerManagementSystemTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create sample plans
        self.plan1 = Plan.objects.create(
            name='Platinum365',
            cost=499,
            validity=365,
            status='Active'
        )
        self.plan2 = Plan.objects.create(
            name='Gold180',
            cost=299,
            validity=180,
            status='Active'
        )

    def test_add_new_customer(self):
        url = reverse('create-customer')
        data = {
              "name": "kdi",
              "dob": "1990-01-01",
              "email": "john@example.com",
              "aadhar_number": "089037676763",
              "registration_date": "2024-03-25",
              "assigned_mobile_number": "8882341568",
              "plan": 1
            }
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Customer.objects.count(), 1)

    def test_list_customer_info(self):
        url = reverse('list-customers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_renew_customer_plan(self):
        # Create a sample customer with a plan
        customer = Customer.objects.create(
            name='Pravin Kedar',
            dob='1992-05-20',
            email='Pravin@example.com',
            aadhar_number='777654321012',
            registration_date='2024-03-01',
            assigned_mobile_number='9876543210',
            plan=self.plan1
        )

        url = reverse('renew-customer-plan', kwargs={'pk': customer.pk})
        data = {
            'renewal_date': '2024-06-01',
            'plan_status': 'Active'
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # def test_upgrade_downgrade_customer_plan(self):
    #     # Create a sample customer with an existing plan
    #     customer = Customer.objects.create(
    #         name='Test User',
    #         dob='1992-05-20',
    #         email='test@example.com',
    #         aadhar_number='987654321012',
    #         registration_date='2024-03-01',
    #         assigned_mobile_number='9966543210',
    #         plan=1
    #     )
    #
    #     url = reverse('upgrade_downgrade_customer_plan', kwargs={'pk': customer.pk})
    #     data = {
    #         'existing_plan_name': 'Silver90',
    #         'new_plan_name': 'Gold180',
    #         'new_plan_cost': '299',
    #         'new_plan_validity': '180',
    #         'new_plan_status': 'Active'
    #     }
    #     response = self.client.post(url, data, content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
    #
    #     # Check if customer's plan has been upgraded
    #     updated_customer = Customer.objects.get(pk=customer.pk)
    #     self.assertEqual(updated_customer.plan_name, 'Gold180')
    #     self.assertEqual(updated_customer.plan_cost, 299)
    #     self.assertEqual(updated_customer.plan_validity, 180)
    #     self.assertEqual(updated_customer.plan_status, 'Active')
