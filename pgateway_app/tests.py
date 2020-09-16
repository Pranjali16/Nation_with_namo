from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from .request_params import *
from .views import TransactionView


class TransactionTestCases(APITestCase):
    """
    Test case is use for testing transaction api
    """

    def setUp(self):
        self.factory = APIRequestFactory()
        self.correct_data = CORRECT_PARAMS
        self.missing_amount = MISSING_AMOUNT
        self.missing_currency = MISSING_CURRENCY
        self.missing_type = MISSING_TYPE
        self.incorrect_card_number = INCORRECT_CARD_NUMBER
        self.missing_card_number = MISSING_CARD_NUMBER
        self.missing_exp_month = MISSING_EXP_MONTH
        self.missing_exp_year = MISSING_EXP_YEAR
        self.missing_cvv = MISSING_CVV

    def test_transaction_with_correct_data(self):
        view = TransactionView.as_view()
        request = self.factory.post(reverse("transaction"), data=self.correct_data, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_with_missing_amount(self):
        view = TransactionView.as_view()
        request = self.factory.post(reverse("transaction"), data=self.missing_amount, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_missing_currency(self):
        view = TransactionView.as_view()
        request = self.factory.post(reverse("transaction"), data=self.missing_currency, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_missing_type(self):
        view = TransactionView.as_view()
        request = self.factory.post(reverse("transaction"), data=self.missing_type, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_incorrect_card_number(self):
        view = TransactionView.as_view()
        request = self.factory.post(reverse("transaction"), data=self.incorrect_card_number, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_missing_card_number(self):
        view = TransactionView.as_view()
        request = self.factory.post(reverse("transaction"), data=self.missing_card_number, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_missing_exp_month(self):
        view = TransactionView.as_view()
        request = self.factory.post(reverse("transaction"), data=self.missing_exp_month, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_missing_exp_year(self):
        view = TransactionView.as_view()
        request = self.factory.post(reverse("transaction"), data=self.missing_exp_year, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_with_missing_cvv(self):
        view = TransactionView.as_view()
        request = self.factory.post(reverse("transaction"), data=self.missing_cvv, format='json')
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)