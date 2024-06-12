from django.urls import path
from . import views

urlpatterns = [
    path('', views.questionario_view, name='questionario_form'),
    path('sucesso/', views.questionario_sucesso, name='questionario_sucesso'),
]
