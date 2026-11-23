"""Find files whose names begin with deep."""
from pathlib import Path


def thats_the_way(folder_path):
    """Return matching file names in the given folder, without recursion."""
    return [item.name for item in Path(folder_path).iterdir()
            if item.is_file() and item.name.startswith("deep")]


if __name__ == "__main__":
    print(thats_the_way(input("Enter folder path: ")))
