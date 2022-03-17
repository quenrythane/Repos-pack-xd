from pliki_pythonowe.my_wikipedia import *

# @app.route('/naruto')
def naruto():
    heroes_list = collect_heroes_list("data/super_heroes.json")
    random_hero = draw_random_hero(heroes_list)
    name, img, summary = find_character_info(random_hero)
    sorted_words_by_length = summary
    return name, img, summary

heroes_list = [naruto(), naruto(), naruto()]
# wylosuj 3 postacie i postuj je aby te największą liczbą wyrazów były pierwsze
sorted_heroes = sorted(heroes_list, key=lambda hero: len(hero[2]), reverse=True)
for name, x, summary in sorted_heroes:
    print(name, len(summary))
