
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views import LinkViewSet, CategoryViewSet, TagViewSet

# API versioning
router = routers.DefaultRouter()
router.register(r'links', LinkViewSet, basename='links')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'tags', TagViewSet, basename='tags')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='Link Room API'))
]