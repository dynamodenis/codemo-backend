from django.conf import settings
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('user/<int:pk>/profile/', views.ProfileAPI.as_view()),  
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)