"""Calculate the cost of ingredients for a recipe."""


def get_recipe_price(prices, optionals=None, **ingredients):
    """Return the total cost, excluding optional ingredients."""
    if optionals is None:
        optionals = []

    total = 0
    for ingredient, price in prices.items():
        if ingredient not in optionals:
            total += price * ingredients[ingredient] / 100

    return total


if __name__ == "__main__":
    print(get_recipe_price(
        {"chocolate": 18, "milk": 8},
        chocolate=200,
        milk=100,
    ))
    print(get_recipe_price(
        {"chocolate": 18, "milk": 8},
        optionals=["milk"],
        chocolate=300,
    ))
    print(get_recipe_price({}))
