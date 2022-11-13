from django.shortcuts import render
from .models import Workout, Exercise
from django.views import generic


class WorkoutList(generic.ListView):

    model = Workout
    template_name = 'index.html'


class ExerciseList(generic.ListView):

    model = Exercise
    template_name = 'exercise_list.html'


class CreateWorkout(generic.CreateView):

    model = Workout
    template_name = 'create_workout.html'


class CreateExercise(generic.CreateView):

    model = Exercise
    template_name = 'create_exercise.html'


