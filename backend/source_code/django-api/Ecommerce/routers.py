from rest_framework import routers
from .Product.views import ProductViewSet, ProductBrandViewSet, ProductCategoryViewSet, ProductSubCategoryViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'product/brand', ProductBrandViewSet)
router.register(r'category', ProductCategoryViewSet)
router.register(r'sub-category', ProductSubCategoryViewSet)
