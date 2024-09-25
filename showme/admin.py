from django.contrib import admin
from .models import ShowMeQuestion

@admin.register(ShowMeQuestion)
class ShowMeQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'option1', 'option2', 'option3', 'correct_answer')