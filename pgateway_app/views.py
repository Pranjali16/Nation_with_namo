from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .utils import TransactionUtility


class TransactionView(APIView):
    """Payment Gateway Transaction View"""

    def post(self, request):
        """ To validate each parameters of request
            To create entry in database
            To update authorization code and status in database
            To give response containing details of transaction"""

        try:
            if request.data["amount"] == "" or \
                    request.data["amount"] is None:
                message = "Error put amount in amount section."
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            else:
                amount = request.data["amount"]
            if request.data["currency"] == "" or \
                    request.data["currency"] is None:
                message = "Error put currency in currency section."
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            else:
                currency = request.data["currency"]
            if request.data["type"] == "" or \
                    request.data["type"] is None:
                message = "Error select card type."
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            else:
                card_type = request.data["type"]
            if request.data["card"]["number"] == "" or \
                    request.data["card"]["number"] is None or len(request.data["card"]["number"])<16:
                message = "Error enter correct card number."
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            else:
                number = request.data["card"]["number"]
            if request.data["card"]["expirationMonth"] == "" or \
                    request.data["card"]["expirationMonth"] is None:
                message = "Error enter expiration month of your card."
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            else:
                exp_month = request.data["card"]["expirationMonth"]
            if request.data["card"]["expirationYear"] == "" or \
                    request.data["card"]["expirationYear"] is None:
                message = "Error enter expiration year of your card."
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            else:
                exp_year = request.data["card"]["expirationYear"]
            if request.data["card"]["cvv"] == "" or \
                    request.data["card"]["cvv"] is None:
                message = "Error enter cvv."
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
            else:
                cvv = request.data["card"]["cvv"]
        except Exception as e:
            message = e.args['message']
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        # To create entry in database based on request
        txn_details = TransactionUtility.create_transaction_entry(amount=amount, currency=currency,
                                                                  card_type=card_type, card_number=number,
                                                                  expiration_month=exp_month,
                                                                  expiration_year=exp_year, cvv=cvv)

        # code to be implemented to payment_transaction() if actual payment is done so taking status as success for now
        payment = TransactionUtility.payment_transaction(amount, currency, card_type, number,
                                                         exp_month, exp_year, cvv)

        # To find txn_id from updated txn_details and then update authorization_code and status.
        # status for now taken as success
        txn_id = txn_details["txn_id"][4:]
        TransactionUtility.update_transaction_entry(int(txn_id),
                                                    authorization_code=txn_details["txn_id"],
                                                    status="success")

        # To update response dict
        response_dict = {
            "amount": txn_details["txn_obj"].amount,
            "currency": txn_details["txn_obj"].currency,
            "type": txn_details["txn_obj"].card_type,
            "card": {
                "number": txn_details["txn_obj"].card_number
            },
            "status": "success",
            "authorization_code": txn_details["txn_id"],
            "time": txn_details["txn_obj"].created_at
        }
        return Response(response_dict, status=status.HTTP_200_OK)