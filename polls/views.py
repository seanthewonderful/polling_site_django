from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
  return HttpResponse("You're looking at question %s." % question_id)
  # The `%` operator in Python is used for string formatting. It allows you to insert values into a string in a specified format. In the example you provided, `%s` is a placeholder that will be replaced by the value of `question_id` when the string is formatted.
  
def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)

