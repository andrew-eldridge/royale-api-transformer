from cards import *
from globaltournaments import *
from locations import *
from clans import *
from rankings import *
from tournaments import *
from format import *


def transform_arena(x):
    arena = ArenaStruct()
    arena.name = x["name"]
    arena.id = x["id"]
    arena.icon_urls = x["iconUrls"]
    return arena


def transform_player(x):
    pass


def transform_player_clan(x):
    pass


def transform_player_league_statistics(x):
    pass


def transform_player_item_level_list(x):
    pass


def transform_player_achievement_badge_list(x):
    pass


def transform_player_achievement_progress_list(x):
    pass


def transform_league_season_result(x):
    pass


def transform_player_item_level(x):
    pass


def transform_player_achievement_badge(x):
    pass


def transform_player_achievement_progress(x):
    pass


def transform_upcoming_chests(x):
    pass


def transform_chest_list(x):
    pass


def transform_chest(x):
    pass


def transform_battle_list(x):
    pass


def transform_battle(x):
    pass


def transform_game_mode(x):
    pass


def transform_player_battle_data_list(x):
    pass


def transform_player_battle_data(x):
    pass
