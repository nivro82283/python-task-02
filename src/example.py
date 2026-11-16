"""Example function and class for the project template."""


def not_a_pep8_fn():
    """Print the example message."""
    print("Linter should error!")


class Example:  # pylint: disable=too-few-public-methods
    """Demonstrate a simple class with one public method."""

    def __init__(self):
        """Initialize the example value."""
        self.x = 6

    def wrong_func(self):
        """Print the example message."""
        print("Linter should error!")


if __name__ == "__main__":
    not_a_pep8_fn()
    Example().wrong_func()
