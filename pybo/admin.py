from django.contrib import admin
from .models import Question



class QuestionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'create_date')
    search_fields = ('subject', 'content')


admin.site.register(Question, QuestionAdmin)

