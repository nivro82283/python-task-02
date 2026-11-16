"""Find files whose names start with 'deep'."""

from pathlib import Path


def thats_the_way(folder_path):
    """
    Return names of files starting with 'deep' in the given folder.

    :param folder_path: Path to the folder to search.
    :return: List of matching file names.
    """
    return [
        item.name
        for item in Path(folder_path).iterdir()
        if item.is_file() and item.name.startswith("deep")
    ]


if __name__ == "__main__":
    folder = input("Enter folder path: ")
    print(thats_the_way(folder))
