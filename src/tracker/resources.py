from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from .models import Category, Transaction


class TransactionResource(resources.ModelResource):
    category = fields.Field(
        column_name="category",
        attribute="category",
        widget=ForeignKeyWidget(Category, field="name"),
    )

    class Meta:
        model = Transaction
        fields = (
            "amount",
            "type",
            "date",
            "category",
        )
