import random
from django.shortcuts import render
from rest_framework import generics
from .models import ShowMeQuestion
from .serializers import ShowMeQuestionSerializer
from rest_framework.permissions import AllowAny


def show_me(request):
    return render(request, 'showme/showme.html')

class ShowMeQuestionList(generics.ListCreateAPIView):
    # queryset = ShowMeQuestion.objects.all()
    serializer_class = ShowMeQuestionSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        questions = list(ShowMeQuestion.objects.all())
        random.shuffle(questions)
        return questions[:5]

class ShowMeQuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShowMeQuestion.objects.all()
    serializer_class = ShowMeQuestionSerializer
    permission_classes = [AllowAny]
