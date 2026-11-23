"""Group iterable items by a supplied key function."""


def group_by(function, iterable):
    """Return lists grouped by hashable function results, retaining item order."""
    groups = {}
    for item in iterable:
        key = function(item)
        groups.setdefault(key, []).append(item)
    return groups


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))
