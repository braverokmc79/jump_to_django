from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from .forms import QuestionForm ,AnswerForm
from .models import Question
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator



def index(request):
     page = request.GET.get('page', '1')  # 페이지
     question_list =Question.objects.order_by('-create_date')
     paginator = Paginator(question_list, 10)  # 10개로 나머지 레스트
     page_obj = paginator.get_page(page)     
     context ={'question_list':page_obj}
     
     return render(request, 'pybo/question_list.html', context)
    
 
def question_create(request):
    if request.method == 'POST':
        form=QuestionForm(request.POST)
        if form.is_valid():  # 폼이 유효하다면
            question = form.save(commit=False) # 임시 저장하여 question 객체를 리턴받는다.
            question.create_date = timezone.now() # 실제 저장을 위해 작성일시를 설정한다.
            question.save()  # 데이터를 실제로 저장한다.
            return redirect('pybo:index')
    else:        
        form =QuestionForm()
    context ={'form':form}    
    return render(request, 'pybo/question_form.html', context)
 
  
    
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers =question.answers.order_by('-create_date')  # ✅ answer_set → answers        
    context = {'question' :question , "answers": answers}
    return render(request, 'pybo/question_detail.html', context)



def answer_create(request, question_id):    
    """
     pybo 답변등록     
    """
    question = get_object_or_404(Question, pk=question_id)    
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else :
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)    
    
    question.answers.create(  # ✅ answer_set → answers
        content=request.POST.get('content'),
        create_date=timezone.now()
    )
    return redirect('pybo:detail', question_id=question.id)






