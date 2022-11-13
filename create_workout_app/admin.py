from django.contrib import admin
from .models import Workout, Exercise


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'published_by', 'created_on')
    list_filter = ('created_on', 'updated_on')
    search_fields = ['title', 'published_by']


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):

    list_display = ('exercise', 'workout', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['exercise', 'workout']

# Register your models here.
