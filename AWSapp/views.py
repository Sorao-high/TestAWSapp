from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question
import random

from django.db.models import Min, Max

def home(request):
    # 'AWSapp/home.html'をレンダリングします
    return render(request, 'AWSapp/home.html')

def quiz(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    total_questions = Question.objects.all().count()
    min_id = Question.objects.all().aggregate(Min('id'))['id__min']
    max_id = Question.objects.all().aggregate(Max('id'))['id__max']

    choices = [
        question.correct_answer,
        question.incorrect_answer1,
        question.incorrect_answer2,
        question.incorrect_answer3,
    ]
    random.shuffle(choices)

    # 次の問題のIDを計算
    question_id = int(question_id)
    next_question_id = question_id + 1
    if next_question_id > max_id:
        next_question_id = min_id

    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        # 正解か不正解かを判定し、結果と次の問題へのリンクを含めたレスポンスを返します。
        if user_answer == question.correct_answer:
            message = "正解です！"
        else:
            message = "残念、不正解です。正解は「{}」です。".format(question.correct_answer)
        return render(request, 'AWSapp/quiz_result.html', {
            'question': question,
            'message': message,
            'next_question_id': next_question_id
        })

    # GETリクエストの場合、問題と選択肢を表示
    return render(request, 'AWSapp/quiz.html', {
        'question': question,
        'choices': choices,
        'next_question_id': next_question_id  # 次の問題へのIDもテンプレートに渡す
    })