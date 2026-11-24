"""Map normalized words to their lengths using comprehensions."""


def long_cat_is_long(text):
    """Lowercase text, remove nonletters except whitespace, and map word lengths.

    Punctuation is deleted rather than turned into a word boundary.
    """
    cleaned = "".join(char for char in text.lower()
                      if char.isalpha() or char.isspace())
    return {word: len(word) for word in cleaned.split()}


count_words = long_cat_is_long  # the function name used in the notebook


if __name__ == "__main__":
    print(long_cat_is_long(input("Enter text: ")))
