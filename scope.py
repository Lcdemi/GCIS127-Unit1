Global_Variable1 = "This is a global variable"
Global_Variable2 = 10
Global_Variable3 = 5.0

def print_param(p): #p = 45
    print(p)
    
def print_local():
    Local_Variable = 30
    print(Local_Variable)
    
def print_which():
    Global_Variable1 = "This is a local variable"
    print(Global_Variable1)
    
def main():
    print_param(Global_Variable1)
    print_param(Global_Variable2) 
    print_param(Global_Variable3)  
    Local_Variable = 15
    print_local()
    print_which()
    print(Global_Variable1)

main()