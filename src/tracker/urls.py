from django.urls import path
from .views import (
    index,
    transactions_list,
    create_transaction,
)


urlpatterns = [
    path("", index, name="index"),
    path("transactions/", transactions_list, name="transactions-list"),
    path("transactions/create/", create_transaction, name="create-transaction"),
]
