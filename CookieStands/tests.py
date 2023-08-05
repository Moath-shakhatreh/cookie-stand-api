from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import CookieStand

from django.contrib.auth.models import User
from django.test.client import Client

# Create your tests here.

class CookieStandsTests(APITestCase):
    
    
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="moath_1", password="marena1"
        )
        testuser1.save()

        test_CookieStands = CookieStand.objects.create(
            location="up_box",
            owner=testuser1,
            description="salty",
            hourly_sales = 2,
            minimum_customers_per_hour = 1,
            maximum_customers_per_hour = 5,
            average_cookies_per_sale = 2,
            )
        test_CookieStands.save()

    def setUp(self) -> None:
        self.client.login(username="moath_1", password="marena1") 


    def test_CookieStands_model(self):
        cookie = CookieStand.objects.get(id=1)
        actual_owner = str(cookie.owner)
        actual_desc = str(cookie.description)
        self.assertEqual(actual_owner, "moath_1")
        self.assertEqual(
            actual_desc, "salty"
        )

    def test_get_CookieStands(self):
        url = reverse("CookieStands_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snacks = response.data
        self.assertEqual(len(CookieStand), 1)
        self.assertEqual(snacks[0]["description"], "salty")
