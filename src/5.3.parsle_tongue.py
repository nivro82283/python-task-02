"""Extract secret messages from a binary file."""


def parsle_tongue(file_path):
    """Yield lowercase messages ending with ! and at least five letters."""
    with open(file_path, "rb") as binary_file:
        message = bytearray()
        current_byte = binary_file.read(1)

        while current_byte:
            if b"a" <= current_byte <= b"z":
                message.extend(current_byte)
            else:
                if current_byte == b"!" and len(message) >= 5:
                    yield message.decode("ascii") + "!"
                message.clear()

            current_byte = binary_file.read(1)


if __name__ == "__main__":
    path = input("Enter image path: ")
    for secret_message in parsle_tongue(path):
        print(secret_message)
