from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.WorkoutList.as_view()), name='home'),
    path('exercise_list/', views.ExerciseList.as_view(), name='exercise_list'),
    path(
        'create_workout/', views.CreateWorkout.as_view(), name='create_workout'
    ),
    path(
        'create_exercise/', views.CreateExercise.as_view(), name='create_exercise'
    ),
    path('<int:pk>/', views.ExerciseDetail.as_view(), name='exercise_detail'),
    path('edit/<int:pk>/', views.ExerciseUpdate.as_view(), name='update_exercise'),
    path('edit_workout/<int:pk>/', views.WorkoutUpdate.as_view(), name='update_workout'),
]