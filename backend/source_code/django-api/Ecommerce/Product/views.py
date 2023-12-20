from rest_framework import viewsets, authentication, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, ProductBrand, ProductCategory, ProductSubCategory
from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import ProductSerializer, ProductBrandSerializer, ProductCategorySerializer, \
    ProductSubCategorySerializer, ProductDetailsSerializer, ProductImageSerializer


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


class ProductDetailsView(APIView):
    def get(self, request, product_id=None, *args, **kwargs):
        if request.method == 'GET':
            if product_id is None:
                product = Product.objects.all()
                serializer = ProductDetailsSerializer(product, many=True)
                return Response(serializer.data)

            else:
                try:
                    product = Product.objects.get(Id=product_id)
                except Product.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = ProductDetailsSerializer(product)
                return Response(serializer.data)


class ProductImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ProductImageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # you can access the file like this from serializer
            # uploaded_file = serializer.validated_data["file"]
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
