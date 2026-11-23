"""Calculate recipe prices from prices per 100 grams."""


def get_recipe_price(prices, optionals=None, **ingredients):
    """Return total cost excluding optionals; missing quantities raise KeyError."""
    if optionals is None:
        optionals = []
    return sum(price * ingredients[name] / 100
               for name, price in prices.items() if name not in optionals)


piece_of_cake = get_recipe_price


if __name__ == "__main__":
    print(get_recipe_price({"chocolate": 18, "milk": 8}, chocolate=200, milk=100))
