##strings and f-strings
first_name = "Deepak"
last_name = "Methalayil"
full_name = f"{first_name} {last_name}" # f is for format. These strings are called format strings
print(full_name)
print(f"Hello,{full_name.title()}")
message = f"Hello,{full_name.title()}!"
print(message)
# f-strings were introduced in python 3.6 .Python 3.5 and earlier we need to use of format()
full_name1 = "{} {}".format(first_name,last_name)
print(full_name1)

