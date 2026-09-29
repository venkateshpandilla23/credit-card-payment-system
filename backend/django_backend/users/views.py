from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiRequest

from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class ProfileView(APIView):
    def get(self, request):
        user = request.user

        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
        })


@extend_schema(
    request=OpenApiRequest(
        request={
            'type': 'object',
            'properties': {
                'refresh': {
                    'type': 'string'
                }
            },
            'required': ['refresh']
        }
    )
)
class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')

            if not refresh_token:
                return Response(
                    {'error': 'Refresh token is required.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {'message': 'Logout successful.'},
                status=status.HTTP_200_OK
            )

        except Exception:
            return Response(
                {'error': 'Invalid or expired refresh token.'},
                status=status.HTTP_400_BAD_REQUEST
            )