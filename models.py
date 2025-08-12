from django.db import models

class Topic(models.Model):
    grade = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Grade {self.grade} - {self.name}"

class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1)
    explanation_a = models.TextField()
    explanation_b = models.TextField()
    explanation_c = models.TextField()
    explanation_d = models.TextField()
    solution = models.TextField()

    def __str__(self):
        return self.text
