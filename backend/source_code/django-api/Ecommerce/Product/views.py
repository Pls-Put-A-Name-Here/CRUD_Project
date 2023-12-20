from rest_framework import viewsets, authentication, permissions, status
from .models import Product, ProductBrand, ProductCategory, ProductSubCategory
from .serializers import ProductSerializer, ProductBrandSerializer, ProductCategorySerializer, \
    ProductSubCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductBrandViewSet(viewsets.ModelViewSet):
    queryset = ProductBrand.objects.all()
    serializer_class = ProductBrandSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductSubCategory.objects.all()
    serializer_class = ProductSubCategorySerializer
