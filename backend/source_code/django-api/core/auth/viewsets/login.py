from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError,InvalidToken
from core.auth.serializers.login import LoginSerializer

class LoginViewSet(ViewSet):
    """
    Login ViewSet
    """
    serializer_class = LoginSerializer
    permission_classes = []
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        """ Login """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)