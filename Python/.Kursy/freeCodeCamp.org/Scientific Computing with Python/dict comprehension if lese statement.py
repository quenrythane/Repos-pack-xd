my_dict = {'a': 1, 'b': 4, 'c':2}

new_dict_with_comprehension = {k: v for k, v in my_dict.items()}
new_dict_with_comprehension_if = {k: v for k, v in my_dict.items() if v > 1}
new_dict_with_comprehension_if_else = {k if v>1 else k*2: v if v>1 else v*10 for k, v in my_dict.items()}
