import sys

def reverse(text):
    return text[::-1]

if __name__ == "__main__":
    try:
        text = sys.argv[1]
    except IndexError:
        text = input("Enter string: ")

    print("Reversed:", reverse(text))
