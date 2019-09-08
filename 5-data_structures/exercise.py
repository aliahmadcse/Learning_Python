from pprint import pprint

sen = 'This is a common interview question'
char_number = {}
for item in sen:
    if item in char_number:
        char_number[item] += 1
    else:
        char_number[item] = 1

sorted_dict = sorted(char_number.items(),
                     key=lambda item: item[1], reverse=True)

pprint(sorted_dict[0],width=10)
