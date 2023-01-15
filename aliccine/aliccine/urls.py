from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from core.views import FoodViewSet
from django.urls import path, include
from rest_framework.routers import SimpleRouter

router = routers.DefaultRouter()
router.register(r'food', FoodViewSet, basename='food')

router = SimpleRouter()
router.register('food', FoodViewSet)
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path("admin/", admin.site.urls),

] 
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)