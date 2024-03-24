from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('list', views.QuizViewset) # router er antena
router.register('category', views.CategoryViewset) # router er antena
router.register('questions', views.QuestionsViewset) # router er antena
router.register('reviews', views.ReviewViewset) # router er antena

urlpatterns = [
    path('', include(router.urls)),
]