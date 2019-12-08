from django.shortcuts import render
from django.http import HttpResponse
from report.task import reportTest
# Create your views here.

def index(request):
  test = reportTest.delay()
  taskID = test.id
  return HttpResponse("hello" + taskID)

def indexTest(request):
  return HttpResponse("hello")

