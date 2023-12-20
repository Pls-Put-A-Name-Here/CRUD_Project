from rest_framework import serializers
from .models import Product, ProductBrand, ProductCategory, ProductSubCategory

"""syntax for serializer
class serializer_name(serializers.ModelSerializer):
    class Meta:
        model = model_name
        fields = '__all__' or ['field1', 'field2', 'field3']
"""


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBrand
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubCategory
        fields = '__all__'