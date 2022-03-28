import wikipedia as wiki
wiki.set_lang('pl')

name = "Naruto Uzumaki"
ita = wiki.suggest(name) or name

print(ita)
