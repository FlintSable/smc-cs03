""" Assignment One: Opening Lines
    Author: Nicholas Noochla-or
    Date: 7/1/2019

    Enhancements in this release:
    - Print a menu
    - Implement convert_units
    - Call convert_units if menu option 0 selected
    - Display converted temperature
"""


def print_header():
    """
    STEM Center Temperature Project
    Nicholas Noochla-or
    """
    print(f"\nSTEM Center Temperature Project \nNicholas Noochla-or")


def print_menu():
    """
    :param
    :return
    :print:
        Main Menu
        ---------
        0 - Convert temperature
        1 - Process a new data file
        2 - Choose units
        3 - Edit room filter
        4 - Show summary statistics
        5 - Show temperature by date and time
        6 - Show histogram of temperatures
        7 - Quit

    """
    output = (
        "\n\nMain Menu\n" +
        "---------\n" +
        "0 - Convert temperature\n" +
        "1 - Process a new data file\n" +
        "2 - Choose units\n" +
        "3 - Edit room filter\n" +
        "4 - Show summary statistics \n" +
        "5 - Show temperature by date and time\n" +
        "6 - Show histogram of temperatures\n" +
        "7 - Quit\n\n" +


        "What is your choice? ")
    print(output, end="")
    pass


def convert_units(celsius_value, units):
    """
    :param
        celsius_value:
            integer or floating point number in celsius
        units:
            - units = 0, return temperature in Celsius (no change)
            - units = 1, return temperature in Fahrenheit
            - units = 2, return temperature in Kelvin
    :return:
        the celsius value returned as Celsius, Fahrenheit or Kelvin
    """
    output = 0.0
    if(units == 0):
        output = celsius_value
    elif(units == 1):
        output = celsius_value * (9/5) + 32
    elif(units == 2):
        output = celsius_value + 273.15
    else:
        return None
    return output


def new_file():
    print("Option 1 selected")


def choose_units():
    print("Option 2 selected")


def change_filter():
    print("Option 3 selected")


def show_summary():
    print("Option 4 selected")


def show_temp_date_time():
    print("Option 5 selected")


def show_histogram():
    print("Option 6 selected")


def exit_program():
    print("Thank you for using the STEM Center Temperature Project")


def main():
    # while True:
    #     try: 
    #         userChoice = int(input("Enter a number "))
    #     except ValueError:
    #         print("Hey, thats not a number!")
    #         continue
    #     twiceNumber = userChoice * 2
        # print("Twice your number is", twiceNumber)
    print_header()
    exec_dict = {
        0 : convert_units,
        1 : new_file,
        2 : choose_units,
        3 : change_filter,
        4 : show_summary,
        5 : show_temp_date_time,
        6 : show_histogram,
        7 : exit_program
    }

    user_menu_input = 1
    while(user_menu_input != 7):
        print_menu()
        user_menu_input = input()

        while(not isinstance(user_menu_input, int) or
              user_menu_input >= 8 or
              user_menu_input < 0):
            try:
                user_menu_input = int(user_menu_input)
                if (user_menu_input >= 8 or user_menu_input < 0):
                    print("Invalid Choice")
                    print_menu()
                    user_menu_input = input()
                    user_menu_input = int(user_menu_input)
            except:
                continue

            try:
                if (not isinstance(user_menu_input, int)):
                    print("*** Please enter a number only ***")
                    print_menu()
                    user_menu_input = input()
            except:
                continue

            try:
                user_menu_input = int(user_menu_input)
            except:
                continue

        if (user_menu_input == 0):
            print("Please enter a temperature in degrees Celsius ", end = "")
            temp_input = input()
            print(f"That's {exec_dict[user_menu_input](float(temp_input), 1)}" + 
                    " degrees Fahrenheit and " + 
                    f"{exec_dict[user_menu_input](float(temp_input), 2)} Kelvin")
        elif (user_menu_input == 1):
            exec_dict[user_menu_input]()
        elif (user_menu_input == 2):
            exec_dict[user_menu_input]()
        elif (user_menu_input == 3):
            exec_dict[user_menu_input]()
        elif (user_menu_input == 4):
            exec_dict[user_menu_input]()
        elif (user_menu_input == 5):
            exec_dict[user_menu_input]()
        elif (user_menu_input == 6):
            exec_dict[user_menu_input]()
        elif (user_menu_input == 7):
            exec_dict[user_menu_input]()


if __name__ == "__main__":
    main()

"""
STEM Center Temperature Project 
Nicholas Noochla-or


Main Menu
---------
0 - Convert temperature
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics 
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 0
Please enter a temperature in degrees Celsius 45
That's 113.0 degrees Fahrenheit and 318.15 Kelvin


Main Menu
---------
0 - Convert temperature
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics 
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 1
Option 1 selected


Main Menu
---------
0 - Convert temperature
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics 
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 2
Option 2 selected


Main Menu
---------
0 - Convert temperature
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics 
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? t
*** Please enter a number only ***


Main Menu
---------
0 - Convert temperature
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics 
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 12
Invalid Choice


Main Menu
---------
0 - Convert temperature
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics 
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? -1
Invalid Choice


Main Menu
---------
0 - Convert temperature
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics 
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 7
Thank you for using the STEM Center Temperature Project
"""