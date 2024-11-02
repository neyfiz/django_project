import os
import django

# Настройка Django для работы в скрипте
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'esports.settings')
django.setup()

from prosettings.models import Game, Team, Player

# Создание тестовых игр
game1 = Game.objects.create(name='Valorant')
game2 = Game.objects.create(name='CS:GO')
game3 = Game.objects.create(name='Call of Duty')

# Создание тестовых команд
team1 = Team.objects.create(name='Natus Vincere', game=game1)
team2 = Team.objects.create(name='FaZe Clan', game=game2)

# Создание тестовых игроков
Player.objects.create(
    name='Pontus Eek', nickname='Zyppan', birth_date='1999-05-15',
    country='Sweden', team=team1, game=game1
)
Player.objects.create(
    name='Ardis Svarenieks', nickname='ardiis', birth_date='1998-11-03',
    country='Latvia', team=team1, game=game1
)
Player.objects.create(
    name='Kyrylo Karasov', nickname='ANGE1', birth_date='1993-10-23',
    country='Ukraine', team=team2, game=game2
)
Player.objects.create(
    name='Andrey Kiprsky', nickname='Shao', birth_date='1996-12-17',
    country='Russia', team=team2, game=game2
)
Player.objects.create(
    name='Dmitry Ilyushin', nickname='SUYGETSU', birth_date='1998-07-22',
    country='Russia', team=None, game=game2
)
Player.objects.create(
    name='Helvijs "broky" Saukants', nickname='broky', birth_date='1999-06-05',
    country='Latvia', team=None, game=game2
)
Player.objects.create(
    name='Matthew "Zywoo" Herbaut', nickname='Zywoo', birth_date='2001-11-09',
    country='France', team=None, game=game3
)

print("Database populated with test data.")
