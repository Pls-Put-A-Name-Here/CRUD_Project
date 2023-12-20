from rest_framework import serializers
from .models import Title, Address, Country, State

"""syntax for serializer
class serializer_name(serializers.ModelSerializer):
    class Meta:
        model = model_name
        fields = '__all__' or ['field1', 'field2', 'field3']
"""


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
