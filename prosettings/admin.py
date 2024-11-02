from django.contrib import admin
from prosettings.models import Player, Team, Game, Organization

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'name', 'team', 'country', 'birth_date')
    search_fields = ('nickname', 'name')
    list_filter = ('team', 'country')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'game', 'logo')
    search_fields = ('name',)
    list_filter = ('organization',)

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')
    search_fields = ('name',)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')
    search_fields = ('name',)
