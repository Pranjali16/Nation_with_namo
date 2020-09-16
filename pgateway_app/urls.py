from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^payment/', TransactionView.as_view(), name='transaction')
]