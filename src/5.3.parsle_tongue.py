"""Extract lowercase secret messages from binary files incrementally."""


def parsle_tongue(file_path):
    """Yield runs of at least five lowercase ASCII letters followed by !."""
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
    for secret in parsle_tongue(input("Enter image path: ")):
        print(secret)
