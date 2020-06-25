from django.urls import path
from .views import (
    LoginAPIView, StudentRegistrationAPIView, MentorRegistrationAPIView, UserRetrieveUpdateAPIView
)

urlpatterns = [
    path('mentor/register/', MentorRegistrationAPIView.as_view()),
    path('student/register/', StudentRegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view(),),
    path('user/', UserRetrieveUpdateAPIView.as_view())
]

