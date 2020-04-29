# example 1

name = input("Enter your name:")
print(f"\nHello!{name.title()}")

# example 2
prompt = "If you tell us who you are, we can personalize the message you see"
prompt += "\n what is your name?"
msg = input(prompt)
print(f"\n Hello, {msg.title()}!")
