from django.db import models


class Question(models.Model):
    subject =models.CharField("제목", max_length=200)
    content =models.TextField("내용",)
    create_date = models.DateTimeField("작성일", auto_now_add=True)
    
    
class Answer(models.Model):
    question =models.ForeignKey(Question, on_delete=models.CASCADE)
    content =models.TextField()
    create_date=models.DateTimeField()
    
    
