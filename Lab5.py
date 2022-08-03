'''This program is designed to output information that is
requested by the user. The user will get statistical plots and
information as it pertains to each section.

'''
#David Warren SDEV 300 April 19 2022
import pandas as pd
import matplotlib.pyplot as plt


def welcome():
    '''This function prints a welcome message.

    This fuction should only be used once.'''

def bye():
    '''This fuction gives user goodbye message.

    This fuction should only be used once.'''
    print("********** Thanks for using the Data Analysis App **********")

def menu_1():
    '''This menu is the first menu seen by the user.

    Take the input of the user and pass to next
    function for validation.'''
    print("Select the file you want to analyze: ")
    print("1. Population Data")
    print("2. Housing Data")
    print("3. Exit the Program")

    selection_1 = input()
    while selection_1 not in ["1","2","3"]:
        selection_1 = input("Please select a value between 1 - 3: ")

    return selection_1

def population_menu():
    '''This is the population menu.

    This menu will print when user selects it.'''

    print("You have entered Population Data.")
    print("Select the Column you want to analyze:")
    print("a. Pop Apr 1")
    print("b. Pop Jul 1")
    print("c. Change Pop")
    print("d. Exit Column")

    pop_selection = input("").lower()
    while pop_selection not in ["a", "b", "c", "d"]:
        pop_selection = input("Please enter a letter a - d: ").lower()
    try:
        data_load = pd.read_csv('PopChange.csv')
    except FileNotFoundError:
        print("Could not find file, " + data_load)
    except IOError:
        print("Could not find file, " + data_load)
    return pop_selection, data_load

def pop_choice(pop_selection,data_load):
    '''This function selects the next function.

    It takes the input and selects the user's input'''
    if pop_selection == "a":
        pop_apr (data_load)
    elif pop_selection == "b":
        pop_jul (data_load)
    elif pop_selection == "c":
        pop_change (data_load)
    elif pop_selection == "d":
        return pop_selection

def housing_menu():
    '''This function takes the user input to make selection

    Stores the users menu selection and returns'''
    print("You have entered Housing Data")
    print("Select the Column you want to analyze: ")
    print("a. Age")
    print("b. Bedrooms")
    print("c. Built")
    print("d. Rooms")
    print("e. Utility")
    print("f. Exit Column")

    house_selection = input("").lower()
    while house_selection not in ["a","b","c","d","e","f"]:
        house_selection = input("Please enter a letter a - f")
    try:
        data_load = pd.read_csv('Housing.csv')
    except IOError:
        print("Could not find file, " + data_load)
    return house_selection, data_load

def pop_apr (data_load):
    '''Loads population data for April.

    Displays data for selected values.'''
    april = pd.DataFrame(data_load)
    april = april['Pop Apr 1']
    print("Count = ",april.count())
    print("Mean = ",april.mean())
    print("Standard Deviation = ",april.std())
    print("Min = ",april.min())
    print("Max = ",april.max())

    plt.hist(april)
    plt.show()

def pop_jul (data_load):
    '''Loads population data for July.

    Displays data for selected values.'''
    july = pd.DataFrame(data_load)
    july = july['Pop Jul 1']
    print("Count = ",july.count())
    print("Mean = ",july.mean())
    print("Standard Deviation = ",july.std())
    print("Min = ",july.min())
    print("Max = ",july.max())

    plt.hist(july)
    plt.show()

def pop_change (data_load):
    '''Loads population change data.

    Displays data for selected values.'''
    change = pd.DataFrame(data_load)
    change = change['Change Pop']
    print("Count = ",change.count())
    print("Mean = ",change.mean())
    print("Standard Deviation = ",change.std())
    print("Min = ",change.min())
    print("Max = ",change.max())

    plt.hist(change)
    plt.show()

def house_choice(house_selection, data_load):
    '''This function takes the user's input and selects.

    Will return original selection if no other selection made.'''
    if house_selection == "a":
        housing_age (data_load)
    elif house_selection == "b":
        housing_bed (data_load)
    elif house_selection == "c":
        housing_built (data_load)
    elif house_selection == "d":
        housing_rooms (data_load)
    elif house_selection == "e":
        housing_utility (data_load)
    elif house_selection == "f":
        return house_selection


def housing_age (data_load):
    '''Loads housing data for April.

    Displays data for selected values.'''
    age = pd.DataFrame(data_load)
    age = age['AGE']
    print("Count = ",age.count())
    print("Mean = ",age.mean())
    print("Standard Deviation = ",age.std())
    print("Min = ",age.min())
    print("Max = ",age.max())

    plt.hist(age)
    plt.show()

def housing_bed (data_load):
    '''Loads housing data for bedrooms.

    Displays data for selected values.'''
    bed = pd.DataFrame(data_load)
    bed = bed['BEDRMS']
    print("Count = ",bed.count())
    print("Mean = ",bed.mean())
    print("Standard Deviation = ",bed.std())
    print("Min = ",bed.min())
    print("Max = ",bed.max())

    plt.hist(bed)
    plt.show()


def housing_rooms (data_load):
    '''Loads housing data for rooms.

    Displays data for selected values.'''
    rooms = pd.DataFrame(data_load)
    rooms = rooms['ROOMS']
    print("Count = ",rooms.count())
    print("Mean = ",rooms.mean())
    print("Standard Deviation = ",rooms.std())
    print("Min = ",rooms.min())
    print("Max = ",rooms.max())

    plt.hist(rooms)
    plt.show()

def housing_built (data_load):
    '''Loads housing data for built.

    Displays data for selected values.'''
    built = pd.DataFrame(data_load)
    built = built['BUILT']
    print("Count = ",built.count())
    print("Mean = ",built.mean())
    print("Standard Deviation = ",built.std())
    print("Min = ",built.min())
    print("Max = ",built.max())

    plt.hist(built)
    plt.show()

def housing_utility (data_load):
    '''Loads housing data for built.

    Displays data for selected values.'''
    utility = pd.DataFrame(data_load)
    utility = utility['UTILITY']
    print("Count = ",utility.count())
    print("Mean = ",utility.mean())
    print("Standard Deviation = ",utility.std())
    print("Min = ",utility.min())
    print("Max = ",utility.max())

    plt.hist(utility)
    plt.show()

def main():
    '''This is the main function.

    This function controls the program'''
    welcome()
    main_exit =""
    while main_exit != "3":
        selection_1 = menu_1()
        if selection_1 == "1":
            pop_selection = ""
            while pop_selection != "d":
                pop_selection, data_load = population_menu()
                pop_choice(pop_selection,data_load)

        elif selection_1 == "2":
            house_selection = ""
            while house_selection != "f":
                house_selection, data_load = housing_menu()
                house_choice(house_selection, data_load)

        elif selection_1 == "3":
            main_exit = "3"
    bye()

main()
