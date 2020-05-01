def make_pizza(size,*flavour):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in flavour:
        print(f"- {topping}")