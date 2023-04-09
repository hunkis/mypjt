from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render, redirect

from .models import Question, Location


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'randing/index.html', context)
    return render(request, 'randing/index.html')

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request):
    if request.method == 'POST':
        sido = request.POST.get('city')
        gugun = request.POST.get('county')
        location = Location(sido=sido, gugun=gugun)
        location.save()
        return render(request, 'randing/result.html')
    else:
        return HttpResponseBadRequest("잘못된 요청입니다.")

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)