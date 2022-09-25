from django.urls import path
from .api import PersonViewSet
from probas import views

urlpatterns = [
    path('decode/', views.decode),
]
