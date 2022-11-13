from django.shortcuts import render
from django.urls import reverse_lazy
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
    fields = ['title', 'featured_image']
    template_name = 'create_workout.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.published_by = self.request.user
        return super().form_valid(form)


class CreateExercise(generic.CreateView):

    model = Exercise
    fields = ['exercise', 'sets', 'reps', 'weight', 'workout']
    template_name = 'create_exercise.html'
    success_url = reverse_lazy('exercise_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        workout = Workout.slug
        return super().form_valid(form)
        form.save(workout)
