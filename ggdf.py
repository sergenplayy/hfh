keyboard_mapping = {
'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е',
'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з',
'[': 'х', ']': 'ї', 'a': 'ф', 's': 'і', 'd': 'в',
'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л',
'l': 'д', ';': 'ж', "'": 'є', 'z': 'я', 'x': 'ч',
'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь',
',': 'б', '.': 'ю', '/': '.'
}
a = 'ghbdsn'
res = ''
for i in a:
    res += keyboard_mapping.get(i,'?')
print(res)
print("good")