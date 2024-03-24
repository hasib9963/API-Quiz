from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission

class CategoryViewset(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    
    
    


class QuizPagination(pagination.PageNumberPagination):
    page_size = 3 # items per page
    page_size_query_param = page_size
    max_page_size = 100

class QuizViewset(viewsets.ModelViewSet):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.QuizSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = QuizPagination
    search_fields = ['category__name', 'quiz__title']


class QuestionsViewset(viewsets.ModelViewSet):
    
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionsSerializer

    
class ReviewViewset(viewsets.ModelViewSet):
    
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer