from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from core.auth.serializers.register import RegisterSerializer

class RegisterViewSet(ViewSet):
    serializer_class = RegisterSerializer
    permission_classes = []
    http_method_names = ['post']
    def create(self, request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            res = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            response = ({
                "refresh": res["refresh"],
                "access": res["access"],
                "user": serializer.data,
                "status":status.HTTP_201_CREATED
            })
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
