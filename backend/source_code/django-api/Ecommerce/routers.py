from rest_framework import routers
from .Product.views import ProductViewSet, ProductBrandViewSet, ProductCategoryViewSet, ProductSubCategoryViewSet, \
    ProductDetailsView, ProductImageView
from .General.views import TitleViewSet, CountryViewSet, StateViewSet, AddressViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'product/brand', ProductBrandViewSet)
router.register(r'category', ProductCategoryViewSet)
router.register(r'sub-category', ProductSubCategoryViewSet)
router.register(r'gen/title', TitleViewSet)
router.register(r'gen/country', CountryViewSet)
router.register(r'gen/state', StateViewSet)

urlpatterns = [path(r'product/details/<int:product_id>', ProductDetailsView.as_view()),
               path(r'product/image', ProductImageView.as_view(), name='product-image')]
