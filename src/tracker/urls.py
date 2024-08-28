from django.urls import path
from .views import (
    index,
    transactions_list,
    create_transaction,
    update_transaction,
    delete_transaction,
    get_transactions,
)


urlpatterns = [
    path("", index, name="index"),
    path("transactions/", transactions_list, name="transactions-list"),
    path("transactions/create/", create_transaction, name="create-transaction"),
    path(
        "transactions/<int:pk>/update/", update_transaction, name="update-transaction"
    ),
    path(
        "transactions/<int:pk>/delete/", delete_transaction, name="delete-transaction"
    ),
    path("get-transactions/", get_transactions, name="get-transactions"),
]
