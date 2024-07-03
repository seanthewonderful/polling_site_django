from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


# Create your views here.
# def index(request):
#   latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
#   context = { "latest_question_list": latest_question_list }
#   return render(request, 'polls/index.html', context)
class IndexView(generic.ListView):
  template_name = "polls/index.html"
  context_object_name = "latest_question_list"
  
  def get_queryset(self):
    return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
  

# def detail(request, question_id):
#   try: 
#     question = Question.objects.get(pk=question_id)
#   except Question.DoesNotExist:
#     raise Http404("Question does not exist")
#   return render(request, 'polls/detail.html', { "question": question })
class DetailView(generic.DetailView):
  model = Question
  template_name = "polls/detail.html"
  
  def get_queryset(self):
    """
    Excludes any questions that aren't published yet.
    """
    return Question.objects.filter(pub_date__lte=timezone.now())

  
# def results(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'polls/results.html', { "question": question })
class ResultsView(generic.DetailView):
  model = Question
  template_name = "polls/results.html"


def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try: 
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # request.POST is a dictionary-like object that lets you access submitted data by key name. In this case, request.POST['choice'] returns the ID of the selected choice, as a string. request.POST values are always strings.
    # request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data.
  except (KeyError, Choice.DoesNotExist):
    # Redisplay the question voting form.
    return render(
      request, 
      'polls/detail.html', 
      {
        'question': question,
        'error_message': "You didn't select a choice.",
      }
    )
  else:
    selected_choice.votes = F('votes') + 1
    # https://docs.djangoproject.com/en/5.0/ref/models/expressions/#f-expressions
    selected_choice.save()
    # Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # reverse() returns a string representing the URL to which the request should be redirected. In this case, it will return "/polls/3/results/" if 3 is question.id
