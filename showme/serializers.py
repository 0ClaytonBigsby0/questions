from rest_framework import serializers
from .models import ShowMeQuestion

class ShowMeQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowMeQuestion
        fields = ['id', 'question', 'option1', 'option2', 'option3', 'correct_answer']