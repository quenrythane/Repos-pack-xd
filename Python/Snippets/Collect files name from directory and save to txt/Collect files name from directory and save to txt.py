import os

path = #"E:\YouTube\.[Na telefonie]\Biznes Od Początku"
file_names_list = os.listdir(path)
txt_file = "text.txt"

file_names_text = "\n".join([name for name in file_names_list])
with open(txt_file , "w", encoding='utf-8') as file:
    file.write(file_names_text)

