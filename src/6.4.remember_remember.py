"""Decode a message stored as black pixels in image columns."""
from PIL import Image


def remember_remember(file_path):
    """Return characters whose code points are black-pixel row indices (channel values 0 or 1).

    Each column must contain exactly one black pixel, otherwise raise ValueError.
    """
    with Image.open(file_path) as original:
        image = original.convert("RGB")
        letters = []
        for column in range(image.width):
            rows = [row for row in range(image.height)
                    if max(image.getpixel((column, row))) <= 1]
            if len(rows) != 1:
                raise ValueError("Each column must contain exactly one black pixel.")
            letters.append(chr(rows[0]))
        return "".join(letters)


if __name__ == "__main__":
    print(remember_remember(input("Enter encoded image path: ")))
