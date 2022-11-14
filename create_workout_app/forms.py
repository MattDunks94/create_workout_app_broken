from django import forms
from .models import Exercise, Workout


class UpdateExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise', 'sets', 'reps', 'weight', 'workout']


class UpdateWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title', 'featured_image']
