from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.NoteList.as_view()),
    path('<int:pk>', views.NoteDetail.as_view()),
]