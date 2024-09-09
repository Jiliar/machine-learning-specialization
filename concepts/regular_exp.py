import re

value = 'hello'
string = 'This is a string with text and hello only this'

if re.findall(value, string):
    print(f'Find word: {value} into string')
else:
    print(f'Don\'t find word: {value} into string')

#get details about string location
print(re.search(value, string))
#output: <re.Match object; span=(31, 36), match='hello'>

string = 'This is a string with numer 114'
print(re.search(f'\d', string))
#output: <re.Match object; span=(28, 29), match='1'>

print(re.search(f'\t', string))
#output: None