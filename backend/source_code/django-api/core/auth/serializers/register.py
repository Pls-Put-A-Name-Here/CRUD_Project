from rest_framework import serializers
from core.user.serializers import UserSerializer
from core.user.models import User

class RegisterSerializer(UserSerializer):
    """
    Registration serializer for requests and user creation
    """
    password = serializers.CharField(write_only=True, required=True, max_length=128, min_length=8)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password','first_name','last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        user = User.objects.create_user(**validated_data)
        return user