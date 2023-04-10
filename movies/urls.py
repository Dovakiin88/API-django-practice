from django.urls import path
from .import views

#NOTE: this is a url configuration
app_name = 'movies'
urlpatterns = [
    path('',views.mainpage, name='main page'),#this represent the root of this app. this to be mapped to the view function we created
    path('<int:movie_id>', views.detail, name='detail')
]