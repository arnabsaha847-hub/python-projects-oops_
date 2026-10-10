
filename = "sample.txt"

try:
    with open(filename, "r") as file:
        text = file.read()

    words = len(text.split())
    lines = len(text.splitlines())
    characters = len(text)

    print("Number of words:", words)
    print("Number of lines:", lines)
    print("Number of characters:", characters)

except FileNotFoundError:
    print("File not found!")
