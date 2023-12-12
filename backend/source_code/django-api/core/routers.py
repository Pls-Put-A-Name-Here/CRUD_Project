from rest_framework import routers
from core.user.viewsets import UserViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.auth.viewsets.login import LoginViewSet
from core.auth.viewsets.refresh import RefreshViewSet
# from core.auth.viewsets import RegisterViewSet,LoginViewSet

router = routers.DefaultRouter()
# User router
router.register(r'users',UserViewSet,basename='user')
router.register(r'auth/register',RegisterViewSet,basename='auth-register')
router.register(r'auth/login',LoginViewSet,basename='auth-login')
router.register(r'auth/refresh',RefreshViewSet,basename='auth-refresh')
urlpatterns = [*router.urls]   