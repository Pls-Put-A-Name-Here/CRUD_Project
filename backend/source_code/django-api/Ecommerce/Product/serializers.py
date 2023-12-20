from rest_framework import serializers
from .models import Product, ProductBrand, ProductCategory, ProductSubCategory, ProductImage

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


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class SimpleProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['Id', 'ImageUrl', 'UploadedOn']


class ProductDetailsSerializer(serializers.ModelSerializer):
    Brand = serializers.StringRelatedField(source='Brand.Name')
    Category = serializers.StringRelatedField(source='Category.Name')
    Subcategory = serializers.StringRelatedField(source='SubCategory.Name')
    images = SimpleProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['Id', 'Name', 'Brand', 'Description', 'Category', 'Subcategory', 'Price', 'images']
