# Dictionary = {
#     'key': 'value',
#     'key': 'value',
# }

# simple Dictionary example
person_detials = {'first_ name': 'deepak', 'last_name': 'methalayil', 'age': 37}
print(person_detials['first_ name'])
print(person_detials['age'])

# for loop in dictionary

favourite_lang = {
    'deepak': 'c',
    'sat': 'go',
    'jjc': 'python',
}
for name, language in favourite_lang.items():
    print(f"{name.title()}'s favourite language is {language.title()}")

# looping through Keys

for name in favourite_lang.keys():
     print(name.title())
# looping through all values

for language in favourite_lang.values():
    print(language.title())
