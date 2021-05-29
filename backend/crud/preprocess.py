import json

lst = []
with open('words.txt', 'r', encoding='utf8') as in_file:
    while True:
        word = in_file.readline().strip('\n')
        if word == '':
            break
        if 2 < len(word) < 6:
            lst.append(word)

with open('words.json', 'w', encoding='utf8') as out_file:
    json.dump(lst, out_file, indent=2, ensure_ascii=False)
