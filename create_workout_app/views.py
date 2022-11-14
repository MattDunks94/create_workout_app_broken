from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import Workout, Exercise
from django.views import generic
from .forms import UpdateExerciseForm, UpdateWorkoutForm


class WorkoutList(generic.ListView):

    model = Exercise
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
        return super().form_valid(form)

    
class ExerciseDetail(generic.DetailView):

    model = Exercise
    template_name = 'exercise_detail.html'


class ExerciseUpdate(generic.UpdateView):

    model = Exercise
    form_class = UpdateExerciseForm
    template_name = 'edit_exercise.html'
    success_url = reverse_lazy('home')


class WorkoutUpdate(generic.UpdateView):

    model = Workout
    form_class = UpdateWorkoutForm
    template_name = 'edit_workout.html'
    success_url = reverse_lazy('home')

    
class DeleteExercise(generic.DeleteView):

    model = Exercise
    template_name = 'delete_exercise.html'
    success_url = reverse_lazy('home')







