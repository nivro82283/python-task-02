"""Calculate the cost of ingredients for a recipe."""


def piece_of_cake(prices, optionals=None, **ingredients):
    """Return the total cost, excluding optional ingredients."""
    if optionals is None:
        optionals = []

    total = 0
    for ingredient, price in prices.items():
        if ingredient not in optionals:
            total += price * ingredients[ingredient] / 100

    return total


get_recipe_price = piece_of_cake  # the function name used in the notebook


if __name__ == "__main__":
    print(piece_of_cake(
        {"chocolate": 18, "milk": 8},
        chocolate=200,
        milk=100,
    ))
    print(piece_of_cake(
        {"chocolate": 18, "milk": 8},
        optionals=["milk"],
        chocolate=300,
    ))
    print(piece_of_cake({}))
