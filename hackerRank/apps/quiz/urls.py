from django.conf.urls import url

from django.urls import path, re_path
from .views import MyQuizListAPI, QuizListAPI, QuizDetailAPI, SaveUsersAnswer, SubmitQuizAPI, AnswersAPI, QuestionsAPI


urlpatterns = [
	path("my-quizzes/", MyQuizListAPI.as_view()),
	path("quizzes/", QuizListAPI.as_view()),
	path("add-questions/", QuestionsAPI.as_view()),
	path("choices/", AnswersAPI.as_view()),
	path("save-answer/", SaveUsersAnswer.as_view()),
	path(r"quizzes/<slug>/", QuizDetailAPI.as_view()),
	re_path(r"quizzes/(?P<slug>[\w\-]+)/submit/$", SubmitQuizAPI.as_view()),
	
]
