raw_text = """
If you've ever spent hours renaming files or updating hundreds of spreadsheet cells, you know how tedious tasks like these can be. But what if you could have your computer do them for you?

In Automate the Boring Stuff with Python, you'll learn how to use Python to write programs that do in minutes what would take you hours to do by hand - no prior programming experience required. Once you've mastered the basics of programming, you'll create Python programs that effortlessly perform useful and impressive feats of automation to:

Search for text in a file or across multiple files
Create, update, move, and rename files and folders
Search the Web and download online content
Update and format data in Excel spreadsheets of any size
Split, merge, watermark, and encrypt PDFs
Send reminder emails and text notifications
Fill out online forms
Step-by-step instructions walk you through each program, and practice projects at the end of each chapter challenge you to improve those programs and use your newfound skills to automate similar tasks.

Don't spend your time doing work a well-trained monkey could do. Even if you've never written a line of code, you can make your computer do the grunt work. Learn how in Automate the Boring Stuff with Python.
"""


def count_words1(raw_text):
    words_list = raw_text.split()
    counter_dict = {}
    for word in words_list:
        if word not in counter_dict:
            counter_dict[word] = 1
        else:
            counter_dict[word] += 1
    sorted_counter_dict = {k: v for k, v in sorted(counter_dict.items(), key=lambda item: item[1], reverse=True)}
    return sorted_counter_dict


def count_words2(raw_text):
    words_list = raw_text.split()
    counter_dict = {}
    for word in words_list:
        counter_dict[word] = counter_dict.get(word, 0) + 1
    sorted_counter_dict = {k: v for k, v in sorted(counter_dict.items(), key=lambda item: item[1], reverse=True)}
    return sorted_counter_dict


print(count_words1(raw_text))
print(count_words2(raw_text))
