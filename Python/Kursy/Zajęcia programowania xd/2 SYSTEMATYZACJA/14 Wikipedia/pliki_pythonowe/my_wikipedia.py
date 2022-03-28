import random
import wikipedia as wiki
wiki.set_lang('pl')  # change language to pl


def collect_heroes_list(path):
    with open(path, 'r') as file:
        heroes_list = [n.strip() for n in file.read().split(',')]
    return heroes_list


def draw_random_hero(heroes_list):
    return random.choice(heroes_list)


def find_character_info(name):
    try:
        content = wiki.summary(name)
    except:
        content = "Nie udało nam się znależć informacji o tej postaci"

    try:
        img = wiki.page(name).images[0]  # url to img
    except:
        img = "https://static.wikia.nocookie.net/shrek/images/a/aa/SoftpawsTransparent.png/revision/latest/top-crop/width/360/height/450?cb=20171222163739"
    return name, img, content


