from django.contrib import admin
from .models import Genre, Movie
# Register your models here.
#NOTE: py manage.py createsuperuser is used to mange users or people that will have access to the site

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'release_year', 'daily_rate','number_in_stock')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)

