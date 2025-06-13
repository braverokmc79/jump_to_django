from django.shortcuts import redirect, render
from .models import Question
from django.shortcuts import get_object_or_404
from django.utils import timezone


def index(request):
     question_list =Question.objects.order_by('-create_date')
     context ={'question_list':question_list}
     return render(request, 'pybo/question_list.html', context)
    
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers =question.answers.order_by('-create_date')  # ✅ answer_set → answers        
    context = {'question' :question , "answers": answers}
    return render(request, 'pybo/question_detail.html', context)



def answer_create(request, question_id):    
    question = get_object_or_404(Question, pk=question_id)    
    question.answers.create(  # ✅ answer_set → answers
        content=request.POST.get('content'),
        create_date=timezone.now()
    )
    return redirect('pybo:detail', question_id=question.id)






