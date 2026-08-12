from re import search

from django.contrib.admin import filters
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    filter_backends= [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['author','category']
    search_fields = ['title','author']
    ordering_fields = ['published_date','title', 'price']
    