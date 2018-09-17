from django.urls import path

from . import views
from .MyOwnTokenGeneration import login

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('login/', login)
]