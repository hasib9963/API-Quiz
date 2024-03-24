# serializers.py
# serializers.py
from rest_framework import serializers
from .models import QuizHistory
from learners.models import UserAccount

class QuizHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizHistory
        fields = '__all__'

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'
