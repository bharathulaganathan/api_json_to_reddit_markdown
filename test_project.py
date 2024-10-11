from project import find_game, key_words


game_id_biz = [
    {'index': 0, 'proper': 'Zenless Zone Zero', 'game': 'zenlesszonezero', 'id': 'U5hbdsT9W7', 'biz': 'nap_global'},
    {'index': 1, 'proper': 'Honkai: Star Rail', 'game': 'starrail', 'id': '4ziysqXOQ8', 'biz': 'hkrpg_global'},
    {'index': 2, 'proper': 'Genshin Impact', 'game': 'genshinimpact', 'id': 'gopR6Cufr3', 'biz': 'hk4e_global'}
]


def test_find_game_zzz():
    assert find_game("zenlesszonezero", key_words, game_id_biz) == game_id_biz[0]
    assert find_game("zzz", key_words, game_id_biz) == game_id_biz[0]
    assert find_game("zenless", key_words, game_id_biz) == game_id_biz[0]
    assert find_game("zone", key_words, game_id_biz) == game_id_biz[0]
    assert find_game("zero", key_words, game_id_biz) == game_id_biz[0]
    assert find_game("u5hbdst9w7", key_words, game_id_biz) == game_id_biz[0]
    assert find_game("nap_global", key_words, game_id_biz) == game_id_biz[0]


def test_find_game_hsr():
    assert find_game("starrail", key_words, game_id_biz) == game_id_biz[1]
    assert find_game("honkai", key_words, game_id_biz) == game_id_biz[1]
    assert find_game("honkai star rail", key_words, game_id_biz) == game_id_biz[1]
    assert find_game("star rail", key_words, game_id_biz) == game_id_biz[1]
    assert find_game("hsr", key_words, game_id_biz) == game_id_biz[1]
    assert find_game("sr", key_words, game_id_biz) == game_id_biz[1]
    assert find_game("4ziysqxoq8", key_words, game_id_biz) == game_id_biz[1]
    assert find_game("hkrpg_global", key_words, game_id_biz) == game_id_biz[1]


def test_find_game_gi():
    assert find_game("genshinimpact", key_words, game_id_biz) == game_id_biz[2]
    assert find_game("genshin", key_words, game_id_biz) == game_id_biz[2]
    assert find_game("impact", key_words, game_id_biz) == game_id_biz[2]
    assert find_game("gi", key_words, game_id_biz) == game_id_biz[2]
    assert find_game("gopr6cufr3", key_words, game_id_biz) == game_id_biz[2]
    assert find_game("hk4e_global", key_words, game_id_biz) == game_id_biz[2]


def test_find_game():
    assert find_game("abc", key_words, game_id_biz) == False
    assert find_game("all", key_words, game_id_biz) == False
    assert find_game("", key_words, game_id_biz) == False