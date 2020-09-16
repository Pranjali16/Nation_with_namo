from django.db import models


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Transaction(BaseModel):
    """ Payment Gateway Model"""

    STATE = (
        ('success', 'success'),
        ('failed', 'failed'),
        ('in-progress', 'In-Progress')
    )
    CARD_TYPE = (
        ('creditcard', 'creditcard'),
        ('debitcard', 'debitcard')
    )

    amount = models.CharField(max_length=255, default="")
    currency = models.CharField(max_length=255, default="")
    card_type = models.CharField(max_length=255, choices=CARD_TYPE, default='creditcard')
    authorization_code = models.CharField(max_length=255, default="")
    card_number = models.CharField(max_length=255, default="")
    expiration_month = models.CharField(max_length=255, default="")
    expiration_year = models.CharField(max_length=255, default="")
    cvv = models.CharField(max_length=255, default="")
    status = models.CharField(max_length=255, choices=STATE, default='success')

    def __str__(self):
        return "%s" % self.created_at
