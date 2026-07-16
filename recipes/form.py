from django import forms
from .models import Recipe, Rating

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'category', 'description', 'ingredients',
                   'instructions', 'image', 'prep_time', 'difficulty']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score', 'comment']