from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsListAPIView.as_view()),
    path('api/newsdetail/<int:pk>/', NewsAPIDetailView.as_view()),
    path('api/createnews/', NewsCreateAPIView.as_view()),

]
