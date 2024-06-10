from django.shortcuts import render
from rest_framework import viewsets
from .serializer import LinkSerializer, CategorySerializer, TagSerializer
from .models import Link, Category, Tag


# Create your views here.

class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    queryset = Link.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
