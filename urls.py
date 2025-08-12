from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.grade_selection, name='grade_selection'),
    path('topics/<int:grade>/', views.topic_selection, name='topic_selection'),
    path('quiz/<int:topic_id>/', views.quiz_view, name='quiz_view'),
]
