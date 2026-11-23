"""Interleave values from multiple iterables."""


def generator_interleaves(*iterables):
    """Yield alternating values, stopping at the shortest iterable."""
    for group in zip(*iterables):
        yield from group


def interleaves(*iterables):
    """Return alternating values as a list; accept one-shot iterables too."""
    return list(generator_interleaves(*iterables))


interleave = interleaves


if __name__ == "__main__":
    print(interleaves("abc", [1, 2, 3], ("!", "@", "#")))
    print(list(generator_interleaves("abc", [1, 2, 3])))
