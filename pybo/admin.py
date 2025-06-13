from django.contrib import admin
from .models import Question, Answer



class QuestionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'create_date')
    search_fields = ('subject', 'content')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'content', 'create_date')
    search_fields = ('content',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

