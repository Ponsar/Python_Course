def make_pizza(size, *toppings):
    """Summarize pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza wiht the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
