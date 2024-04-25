def bday_message():
    my_name = input("Please enter your name: ")
    birth_month = input("Please enter your birth month: ")
    birth_day = input("Please enter your birth day: ")
    birth_year = input("Please enter your birth year: ")
    print(my_name, ", your birthday is on " , birth_month, " ", birth_day, ", ", birth_year, "!", sep="")

def main():
    bday_message()
main()