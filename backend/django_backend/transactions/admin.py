from django.contrib import admin
from django.http import HttpResponse
import csv

from .models import Transaction


def export_transactions_csv(modeladmin, request, queryset):
    response = HttpResponse(
        content_type='text/csv'
    )

    response['Content-Disposition'] = (
        'attachment; filename="transactions.csv"'
    )

    writer = csv.writer(response)

    writer.writerow([
        'ID',
        'User',
        'Card',
        'Amount',
        'Status',
        'Transaction Reference',
        'Created At'
    ])

    for transaction in queryset:
        writer.writerow([
            transaction.id,
            transaction.user.username,
            transaction.card.id,
            transaction.amount,
            transaction.status,
            transaction.transaction_reference,
            transaction.created_at
        ])

    return response


export_transactions_csv.short_description = "Export selected transactions to CSV"


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'card',
        'amount',
        'status',
        'transaction_reference',
        'created_at',
    )

    list_filter = (
        'status',
        'created_at',
    )

    search_fields = (
        'user__username',
        'transaction_reference',
    )

    ordering = (
        '-created_at',
    )

    actions = [
        export_transactions_csv
    ]