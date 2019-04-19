import re

string = "'I\'M NOT SCREAMING', she said. But it was a LIE."
print('TEMPLATE: ', string + '\n')

print('Remove uppercase letters:')
print(re.sub('[A-Z]', '', string) + '\n')

print('Remove lowercase letters:')
print(re.sub('[a-z]', '', string) + '\n')

print('Remove ponctuation characters:')
print(re.sub('[,.\']', '', string) + '\n')

print('Remove ponctuation + letters:')
print(re.sub('[,.\'a-zA-Z]', '', string) + '\n')

print('Remove spaces:')
print(re.sub('[" "]', '', string) + '\n')  # string.replace(" ", '')

string += '24 .3, - 234 00_0'
print('NEW TEMPLATE: ', string + '\n')

print('Remove numbers:')
print(re.sub('[0-9]', '', string) + '\n')

print('Keep only numbers:')
print(re.sub('[^0-9]', '', string) + '\n')

