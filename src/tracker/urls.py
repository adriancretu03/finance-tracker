from django.urls import path

from .views import (create_transaction, delete_transaction, get_transactions,
                    index, transactions_charts, transactions_export,
                    transactions_list, update_transaction)

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
    path("transactions/charts", transactions_charts, name="transactions-charts"),
    path("transactions/export", transactions_export, name="transactions-export"),
]
