from django.shortcuts import render, get_object_or_404
import random
from .models import Topic, Question

def grade_selection(request):
    grades = [8, 9]
    return render(request, 'grade_selection.html', {'grades': grades})

def topic_selection(request, grade):
    topics = Topic.objects.filter(grade=grade)
    return render(request, 'topic_selection.html', {'topics': topics, 'grade': grade})

def quiz_view(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    questions = list(Question.objects.filter(topic=topic))
    random.shuffle(questions)
    questions = questions[:10]
    return render(request, 'quiz.html', {'topic': topic, 'questions': questions})
