def add_chars(char1, char2):
    solution = ord(char1) + ord(char2)
    print(char1, "+", char2, "=", solution)
    character = chr(solution)
    print("Your associated character is:", character)

def subtract_chars(char1, char2):
    solution = ord(char1) - ord(char2)
    print(char1, "-", char2, "=", solution)
    character = chr(solution)
    print("Your associated character is:", character)

def main():
    char1 = input("Please enter a character: ")
    char2 = input("Please enter another character: ")
    add_chars(char1, char2)
    subtract_chars(char1, char2)

main()

#nothing may be showing up because when adding/subtracting two letters together based on ASCII values, those new values 
#may end up out of range from the regular ASCII table values, therefore causing nothing or weird symbols to show

#A TypeError will be raised if more than one character is input into an ord function because there are no ASCII
#values for multiple characters, only for one character. Multiple characters do not have an ASCII value, therefore
#cannot be given an ASCII value by the ord function and cause an error