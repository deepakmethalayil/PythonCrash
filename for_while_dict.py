member_skill_enhancement = {}
response = True
while response:
    # taking inputs from user
    name = input("\n what is your name?")
    technology = input("which technology would you like to learn?")
    member_skill_enhancement[name] = technology

    # Taking another person
    user_input = input("would you like to add another person?(yes/no):")
    if user_input == 'no':
        response = False

# show results
for name, technology in member_skill_enhancement.items():
    print(f"{name.title()} would like to learn {technology.title()}")
