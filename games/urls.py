from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_index),
    path('add_game', views.add_a_game),
    path('create_game', views.create_game),
    path('<int:game_id>/view', views.view_game),
    path('<int:game_id>/edit', views.edit_game),
    path('<int:game_id>/update', views.update_game),
    path('<int:game_id>/delete', views.delete_game),

]