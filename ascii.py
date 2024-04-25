A_in_ASCII = ord("A") #declared global variable

def convert_to_ascii(character):
    number = ord(character)
    print(number)

def convert_from_ascii(code):
    character = chr(code)
    print(character)

def alphabet_position(letter, A_in_ASCII):
    position = ord(letter) - A_in_ASCII + 1
    print(letter, "is in position", position)

def main():
    character = input("Enter a character: ")
    convert_to_ascii(character)

    code = input("Enter a code: ")
    code = int(code)
    convert_from_ascii(code)

    alphabet_position(character, A_in_ASCII)
    alphabet_position(character, 87)
    alphabet_position(character, 48)

main()