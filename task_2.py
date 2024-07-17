num_1 = int(input("Enter a first number:"))
num_2 = int(input("Enter a second number:"))
print("\n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Modulus \n6.Exponentiation \n7.Floor division")


def calc():
    
        opt = int(input("\nEnter a number for choosing calculation"))
        match opt:
            case 1:
                print("Addition:", num_1+num_2)
            case 2:
                print("Subtraction:", num_1-num_2)
            case 3:
                print("Multiplication:", num_1*num_2)
            case 4:
                print("Division:", num_1/num_2)
            case 5:
                print("Modulus:", num_1%num_2)
            case 6:
                print("Exponentiation:", num_1**num_2)
            case 7:
                print("Floor Division:", num_1//num_2)
            case _:
                print("Invalid number..... Please enter a valid number!")

n= int(input("How many times wants to calculate ?"))
for i in range(n):
    calc()
    
