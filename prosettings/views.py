from django.shortcuts import render, get_object_or_404
from .models import Team, Player, Game, Organization

def index(request):
    return render(request, 'prosettings/index.html')

def organizations(request):
    organizations = Organization.objects.all()
    return render(request, 'prosettings/organizations.html', {'organizations': organizations})

def organization_detail(request, org_id):
    organization = get_object_or_404(Organization, id=org_id)
    teams = organization.teams.all()
    players = Player.objects.filter(team__in=teams).distinct()
    return render(request, 'includes/organization_detail.html', {
        'organization': organization,
        'teams': teams,
        'players': players
    })

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    players = team.players.all()
    organization = team.organization
    return render(request, 'includes/team_detail.html', {
        'team': team,
        'players': players,
        'organization': organization
    })


def players(request):
    players = Player.objects.all()
    return render(request, 'prosettings/players.html', {'players': players})


def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    return render(request, 'includes/player_detail.html', {'player': player})


def games(request): 
    games = Game.objects.all()
    return render(request, 'prosettings/games.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    return render(request, 'includes/game_detail.html', {'game': game})

