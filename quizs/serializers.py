from rest_framework import serializers
from . import models

class QuizCreatorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    quiz = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField(many=False, source='catagory')  # Corrected field name
    questions = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Quiz
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source='catagory.name')  # Corrected source
    
    class Meta:
        model = models.Quiz
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'