from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.db.models import Sum
from django.utils import timezone
from django.shortcuts import redirect

from transactions.models import Transaction


class DailyPaymentSummary(Transaction):
    class Meta:
        proxy = True
        verbose_name = "Daily Payment Summary"
        verbose_name_plural = "Daily Payment Summary"


@admin.register(DailyPaymentSummary)
class DailyPaymentSummaryAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()

        custom_urls = [
            path(
                'summary/',
                self.admin_site.admin_view(self.daily_summary),
                name='daily-payment-summary',
            ),
        ]

        return custom_urls + urls

    def changelist_view(self, request, extra_context=None):
        return redirect('admin:daily-payment-summary')

    def daily_summary(self, request):
        today = timezone.localdate()

        transactions = Transaction.objects.filter(
            created_at__date=today
        )

        total_transactions = transactions.count()

        successful_payments = transactions.filter(
            status='SUCCESS'
        ).count()

        failed_payments = transactions.filter(
            status='FAILED'
        ).count()

        pending_payments = transactions.filter(
            status='PENDING'
        ).count()

        total_amount = transactions.aggregate(
            total=Sum('amount')
        )['total'] or 0

        context = {
            **self.admin_site.each_context(request),
            'title': 'Daily Payment Summary',
            'today': today,
            'total_transactions': total_transactions,
            'successful_payments': successful_payments,
            'failed_payments': failed_payments,
            'pending_payments': pending_payments,
            'total_amount': total_amount,
        }

        return TemplateResponse(
            request,
            'admin/daily_payment_summary.html',
            context,
        )