from pliki_pythonowe.my_wikipedia import *

# @app.route('/naruto')
def naruto():
    heroes_list = collect_heroes_list("dane/super_heroes.json")
    random_hero = draw_random_hero(heroes_list)
    name, img, summary = find_character_info(random_hero)
    return name, img, summary
