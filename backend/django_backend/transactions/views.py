from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Transaction
from .serializers import TransactionSerializer


@extend_schema(
    parameters=[
        OpenApiParameter(
            name='status',
            type=str,
            required=False,
            description='Filter by transaction status: PENDING, SUCCESS, or FAILED'
        ),
        OpenApiParameter(
            name='min_amount',
            type=float,
            required=False,
            description='Minimum transaction amount'
        ),
        OpenApiParameter(
            name='max_amount',
            type=float,
            required=False,
            description='Maximum transaction amount'
        ),
        OpenApiParameter(
            name='start_date',
            type=str,
            required=False,
            description='Start date in YYYY-MM-DD format'
        ),
        OpenApiParameter(
            name='end_date',
            type=str,
            required=False,
            description='End date in YYYY-MM-DD format'
        ),
    ]
)
class TransactionHistoryView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Transaction.objects.filter(
            user=self.request.user
        ).order_by('-created_at')

        status = self.request.query_params.get('status')
        min_amount = self.request.query_params.get('min_amount')
        max_amount = self.request.query_params.get('max_amount')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if status:
            queryset = queryset.filter(status=status)

        if min_amount:
            queryset = queryset.filter(amount__gte=min_amount)

        if max_amount:
            queryset = queryset.filter(amount__lte=max_amount)

        if start_date:
            queryset = queryset.filter(created_at__date__gte=start_date)

        if end_date:
            queryset = queryset.filter(created_at__date__lte=end_date)

        return queryset