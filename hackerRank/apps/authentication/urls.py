from django.urls import path
from .views import ( StudentRegistrationAPIView, MentorRegistrationAPIView, UserRetrieveUpdateAPIView )
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('mentor/register/', MentorRegistrationAPIView.as_view()),
    path('student/register/', StudentRegistrationAPIView.as_view()),
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/token/', TokenRefreshView.as_view()),
]
