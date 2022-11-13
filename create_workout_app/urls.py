from . import views
from django.urls import path


urlpatterns = [
    path('', views.WorkoutList.as_view(), name='home'),
    path('exercise_list/', views.ExerciseList.as_view(), name='exercise_list'),
]