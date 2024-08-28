from django.urls import path
from .views import (
    index,
    transactions_list,
)


urlpatterns = [
    path("", index, name="index"),
    path("transactions/", transactions_list, name="transactions-list"),
]
