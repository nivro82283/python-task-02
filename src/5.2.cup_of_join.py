"""Combine lists with a separator between each pair."""


def join(*lists, sep="-"):
    """Return a new combined list, or None when no lists are supplied."""
    if not lists:
        return None
    result = []
    for index, current in enumerate(lists):
        if index:
            result.append(sep)
        result.extend(current)
    return result


cup_of_join = join


if __name__ == "__main__":
    print(join([1, 2], [8], [9, 5, 6], sep="@"))
