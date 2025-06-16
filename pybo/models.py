from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author =models.ForeignKey(User,  on_delete=models.CASCADE, null=True)
    subject = models.CharField("제목", max_length=200)
    content = models.TextField("내용")
    create_date = models.DateTimeField("작성일", auto_now_add=True)

    #class Meta:
        #verbose_name = "질문"
        #verbose_name_plural = "질문 목록"

    def __str__(self):
        return f"[{self.id}] {self.subject}"


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        verbose_name="질문",
        on_delete=models.CASCADE,
        related_name="answers"
    )
    content = models.TextField("답변 내용")
    create_date = models.DateTimeField("작성일")

    #class Meta:
        #verbose_name = "답변"
        #verbose_name_plural = "답변 목록"

    def __str__(self):
        return f"[답변] {self.content[:30]}..."
