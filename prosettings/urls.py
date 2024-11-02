from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('organizations/', views.organizations, name='organizations'),
    path('organization/<int:org_id>/', views.organization_detail, name='organization_detail'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail'),
    path('players/', views.players, name='players'),
    path('player/<int:player_id>/', views.player_detail, name='player_detail'),
    path('games/', views.games, name='games'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
]