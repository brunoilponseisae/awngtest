from django.http import HttpResponse
from .models import Question


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def questions(request):
    questions = Question.objects.all()
    res = ""
    for question in questions:
        res = f"{res}{question.question_text}<br/>"

    return HttpResponse(res)