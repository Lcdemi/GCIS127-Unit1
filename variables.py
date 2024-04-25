def variable_practice():
    age_in_months = 229
    days_in_year = 365
    first_pet = "Leia"
    first_five_digits_pi = 3.1415
    print(age_in_months, days_in_year, first_pet, first_five_digits_pi)

def expressions_practice():
    age_expression = 15 + 4
    remainder = 19 % 4
    two_cubed = 2 ** 3
    random_problem = 6 * (9 + 12) - 6
    print(age_expression, remainder, two_cubed, random_problem)

def prompt_and_print(): #this program now runs because of the float cast
    variable1 = input("Enter a numeric value: ")
    variable2 = input("Enter a second numeric value: ")

    variable1 = float(variable1) #casts values to a float
    variable2 = float(variable2)

    print(variable1, "+", variable2, "=", (variable1 + variable2))
    print(variable1, "-", variable2, "=", (variable1 - variable2))
    print(variable1, "*", variable2, "=", (variable1 * variable2))
    print(variable1, "/", variable2, "=", (variable1 / variable2))


def main():
    variable_practice()
    expressions_practice()
    prompt_and_print()

main()