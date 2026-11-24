"""Join lists with a separator between them."""


def cup_of_join(*lists, sep="-"):
    """Return a combined list, or None when no lists are provided."""
    if not lists:
        return None

    result = []
    for index, current_list in enumerate(lists):
        if index > 0:
            result.append(sep)
        result.extend(current_list)

    return result


join = cup_of_join  # the function name used in the notebook


if __name__ == "__main__":
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep="@"))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([1]))
    print(cup_of_join())
