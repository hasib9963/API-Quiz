# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import QuizHistory
from learners.models import UserAccount
from .serializers import QuizHistorySerializer, UserAccountSerializer

# class QuizHistoryViewSet(viewsets.ModelViewSet):
#     queryset = QuizHistory.objects.all()
#     serializer_class = QuizHistorySerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)

# class UserAccountViewSet(viewsets.ModelViewSet):
#     queryset = UserAccount.objects.all()
#     serializer_class = UserAccountSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return self.queryset.filter(user=self.request.user)


# views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import QuizHistorySerializer, UserAccountSerializer

class QuizHistoryViewSet(viewsets.ModelViewSet):
    queryset = QuizHistory.objects.all()
    serializer_class = QuizHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter queryset based on the currently authenticated user
        return self.queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch UserAccount object for the currently authenticated user
        try:
            user_account = UserAccount.objects.get(user=self.request.user)
            context['user_data'] = UserAccountSerializer(user_account).data
        except UserAccount.DoesNotExist:
            context['user_data'] = None
        return context
