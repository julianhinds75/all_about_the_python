# # Importing the math module for advanced math operations

import math

while True:
    print("\nChoose a math operation. \n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division"
          "\n4 - Modulo \n5 - Raising to the power\n6 - Square root\n7 - Logarithm"
          "\n8 - Sine\n9 - Cosine\n10 - Tangent\n")
    oper = input("\nYour option from the menu: ")

    # Addtion

    if oper == "0":
        val1 = float(input("\nFirst value: ")) #using float to change the value from a sting to float
        val2 = float(input("\nSecond value: "))

        print("\nResult of {} + {} is: ".format(val1, val2) + str(val1 + val2) + "\n")

        # Going back to the menu
        back = input("\nReturn to menu? (Y/N) ")

        if back.casefold() == "y":
            continue
        else:
            print("\nThank you for using this calc, goodbye")
            break

    # Subtraction

    elif oper == "1":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nResult  of {} - {} is: ".format(val1, val2) + str(val1 - val2) + "\n")

        # Going back to the menu
        back = input("\nReturn to menu? (Y/N) ")

        if back.casefold() == "y":
            continue
        else:
            print("\nThank you for using this calc, goodbye")
            break


    # Multiplication

    elif oper == "2":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nResult of {} * {} is: ".format(val1, val2) + str(val1 * val2) + "\n")

        # Going back to the menu
        back = input("\nReturn to menu? (Y/N) ")

        if back.casefold() == "y":
            continue
        else:
            print("\nThank you for using this calc, goodbye")
            break



    # Division

    elif oper == "3":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nResult of {} / {} is: ".format(val1, val2) + str(val1 / val2) + "\n")

        # Going back to the menu
        back = input("\nReturn to menu?: (Y/N) ")

        if back.casefold() == "y":
            continue
        else:
            print("\nThank you for using this calc, goodbye")
            break


    # Modulo

    elif oper == "4":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nResult of {} / {} is: ".format(val1, val2) + str(val1 % val2) + "\n")

        # Going back to the menu
        back = input("\nReturn to meun?: (Y/N) ")

        if back.casefold() == "y":
            continue
        else:
            print("\nThank you for using this calc, goodbye")
            break



    # Raising to a power

    elif oper == "5":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))

        print("\nResult of {} to the power of {} is: ".format(val1, val2) + str(math.pow(val1, val2)) + "\n")

        # Going back to the menu
        back = input("\nReturn to menu?: (Y/N) ")

        if back.casefold() == "y":
            continue
        else:
            print("\nThank you for using this calc, goodbye")
            break


    # Square root

    elif oper == "6":
        val1 = float(input("\nEnter the number that you want the square root of: "))

        print("\nThe square root of {} is: ".format(val1) + str(math.sqrt(val1)) + "\n")

        # Going back to the menu
        back = input("\nReturn to menu: (Y/N) ")

        if back.casefold() == "y":
            continue
        else:
            print("\nThank you for using this calc, goodbye")
            break


    # Logarithm to base 2

    elif oper == "7":
        val1 = float(input("\nEnter the number that you want the logarithm result of: "))

        print("\nThe logarithm result of {} is: ".format(val1) + str(math.log(val1, 2)) + "\n")

        # Going back to the menu
        back = input("\nReturn to menu: (Y/N) ")

        if back.casefold() == "y":
            continue
        else:
            print("\nThank you for using this calc, goodbye")
            break


    # Sine, angles I think

    elif oper == "8":
        val1 = float(input("\nEnter the value (in degrees) for calculating the sine: "))

        print("\nThe result is: " + str(math.sin(math.radians(val1))) + "\n")

        # Going back to the menu
        back = input("\nReturn to menu: (Y/N) ")

        if back.casefold() == "y":
            continue
        else:
            print("\nThank you for using this calc, goodbye")
            break

    # cosine

    elif oper == "9":
        val1 = float(input("\nEnter the value (in degrees) for calculating the cos: "))

        print("\nThe result is: " + str(math.cos(math.radians(val1))) + "\n")

        # Going back to the menu
        back = input("\nReturn to menu: (Y/N) ")

        if back.casefold() == "y":
            continue
        else:
            print("\nThank you for using this calc, goodbye")
            break



    # Tangent

    elif oper == "10":
        val1 = float(input("\nEnter the value (in degrees) for calculating the cos: "))

        print("\nThe result is: " + str(math.tan(math.radians(val1))) + "\n")

        # Going back to the menu
        back = input("\nReturn to menu: (Y/N) ")

        if back.casefold() == "y":
            continue
        else:
            print("\nThank you for using this calc, goodbye")
            break

    # Handling invalid options
    else:
        print("\nThis is an invalid option. Please select from the menu\n")
        continue

# End of program



































































