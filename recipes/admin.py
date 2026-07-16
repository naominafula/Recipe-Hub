from django.contrib import admin
from .models import Recipe, Category, Rating

admin.site.register(Category)
admin.site.register(Rating)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'difficulty', 'created_at')
    list_filter = ('category', 'difficulty')
    search_fields = ('title', 'ingredients')