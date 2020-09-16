# README #

This README would normally document the details of application, classes, methods, api and end points.


### Dependencies ###

* Python 3.x
* PostGreSQL 12.x

### Running Sample API from DRF ###

Url for transaction api
* Go to http://127.0.0.1:8000/nationwithnamo/payment/

### Contribution guidelines ###

There are 9 test cases
* Running tests: "python manage.py test"

### Classes and Methods###

Classes:

- TransactionView: view class which handles the post request.
- TransactionView: utils class which is having methods which works on database.

Methods:

- create_transaction_entry(): which will create entry in database based on request.
- update_transaction_entry(): which will update authorization code and status in database. 

# Note
- payment_transaction(): is just a demo function which is not implemented because it has to be made for actual payment.
