import re


def repeated_word(input):

    duplicates_list=[]
    input = re.sub(r"[^A-z|\s]", '', input)
    input = input.lower()
    input = input.split()

    for i in input:
        if i in duplicates_list :
            return i
        else:
            duplicates_list.append(i)

print(repeated_word("Khaled is a huge fan of Valencia and Milan clubs, but Milan is his favorite"))
