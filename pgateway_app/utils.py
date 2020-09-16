from pgateway_app.models import *


class TransactionUtility:
    """ Transaction utility"""

    @staticmethod
    def create_transaction_entry(**kwargs):
        """To create entry in Transaction database"""
        try:
            txn_obj = Transaction.objects.get(**kwargs)
        except:
            txn_obj = Transaction.objects.create(**kwargs)
        result = {
            "txn_id": "TEST" + str(txn_obj.id),
            "txn_obj": txn_obj
        }
        return result

    @staticmethod
    def update_transaction_entry(txn_id, **kwargs):
        """ To update authorization_code and status for transaction"""
        try:
            Transaction.objects.filter(id=txn_id).update(**kwargs)
        except:
            print("Transaction has not done")

    @staticmethod
    def payment_transaction(*args):
        """code to be implemented if actual payment is done"""
        pass