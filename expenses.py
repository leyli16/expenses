# Student Name in Canvas: Le Li
# Penn ID: 40053122
# Did you do this homework on your own (yes / no): Yes
# Resources used outside course materials: TA Recitation

"""
This Python exam will involve implementing a system for managing expenses.  You will
download the skeleton of the program, then implement the functions.  The design of the
program has been set up for you.

In this system, users will be able to add and deduct expenses, update expenses, sort expenses,
and export filtered expenses to a file.  The program will initially load a collection of expenses
from 2 different .txt files (in the same format) and store them in a dictionary.

NOTE(S):
- It is important that you DO NOT edit the expenses.txt file or the expenses_2.txt file.  If you do,
you could fail the automated testing.
- DO NOT change the spacing or remove any blank lines.
- DO NOT copy/paste the text from the expenses.txt file or the expenses_2.txt file into another file.
"""


def init_file(file):
    """
    A helper function: loads the given file and returns the lines as list
    """
    # open file in read mode
    f = open(file, 'r')

    # read each lines and store into lines
    lines = f.readlines()

    # close the file
    f.close()

    return lines


def round_balance(expenses, expenses_type):
    '''Rounds the expenses amount balance of the given expenses_type to two decimal places.
    updates the expenses amount in the expenses dictionary.
    '''

    expenses[expenses_type] = round(expenses[expenses_type], 2)


def import_expenses(expenses, file):
    """Reads data from the given file and stores the expenses in the given expenses dictionary,
    where the expense type is the key and the total expense amount for that expense is the value.

    The same expense type may appear multiple times in the given file.

    Ignores expenses with missing amounts. If a line contains both an expense type and an expense amount,
    they will be separated by a colon (:).

    You can assume that if they exist, expense types are one-word strings and the amounts are numerical.

    Strip any whitespace before or after the expense types and amounts.

    Blank lines should be ignored.

    Expenses are case sensitive. "coffee" is a different expense from "Coffee"

    Note: This function will be called twice in main with the same dictionary but different files.

    This function doesn’t return anything.  Rather, it updates the given expenses dictionary based
    on the expenses in the given file.
    """

    # load expenses file
    expenses_lines = init_file(file)


    for line in expenses_lines:
        # remove whitespace at the beginning and end of a string
        line = line.rstrip()

        # if this line is empty, skip to the next one
        if line == '':
            continue

        # split the line into a list which is separated by ':'
        expense_info = line.split(':')
        # get expenses type which is the key
        expense_type = expense_info[0].strip()
        # get expenses amount which is the value
        expense_amount = expense_info[1].strip()

        # cast expenses amount into float
        try:
            expense_amount = float(expense_amount)
        except:
            expense_amount = 0

        # update each expenses type and associated amount to expenses {}
        if expense_type not in expenses:
            expenses[expense_type] = expense_amount
        else:
            expenses[expense_type] += expense_amount

        # round expenses amount into two decimal
        round_balance(expenses, expense_type)


def get_expense(expenses, expense_type):
    """Prints and returns the value for the given expense type in the given expenses dictionary.

    Prints a friendly message and returns None if the expense type doesn't exist. (Note: Printing a friendly message
    means that the program should not raise an error or otherwise terminate. Simply tell the user that the requested
    expense type does not exist and continue the program. Also note that None is a specific keyword in Python of
    NoneType. You should not return a string “None” from this function.)
    """

    # if there is no such expense type
    if expenses.get(expense_type) == None:
        print("Sorry, that expense type doesn't exist.")
        return  # stop here and return None

    # otherwise return the info
    return expenses.get(expense_type)


def add_expense(expenses, expense_type, value):
    """Adds the given expense type and value to the given expenses dictionary.

    If the expense type already exists, add the value to the total amount.

    Otherwise, creates a new expense type with the value.

    Prints the expense amount.

    This function doesn’t return anything.
    """

    # if there is no such expense type
    if expenses.get(expense_type) == None:
        expenses[expense_type] = value
    else:
        # add value into the given expenses type
        expenses[expense_type] += value

    # round the amount to 2 decimals
    round_balance(expenses, expense_type)

    # print the updated expense amount.
    print("Expense: ", expenses[expense_type])


def deduct_expense(expenses, expense_type, value):
    """Deducts the given value from the given expense type in the given expenses dictionary.

    Raises a RuntimeError if the value is greater than the existing total of the expense type. Note: You are not
    supposed to use try/except to catch the RuntimeError you raised. We expect the function to raise a RuntimeError
    if the value is greater than the existing total of the expense type.

    Prints a friendly message if the expense type doesn't exist. (Note: Printing a friendly message means that the
    program should not raise an error or otherwise terminate. Simply tell the user that the requested expense type
    does not exist and continue the program.)

    Print the updated expense amount if runtime error is not raised.

    This function doesn’t return anything.
    """

    existing_expense_amount = expenses.get(expense_type)

    # if there is no such expense type
    if existing_expense_amount == None:
        print("Sorry, that expense type does not exist.")
        return

    # if the value is greater than the existing expense amount
    if value > existing_expense_amount:
        raise RuntimeError('Amount greater than the existing total of the expense type.')

    # deduct the amount from the existing_expense_amount
    expenses[expense_type] -= value

    # round the amount to 2 decimals
    round_balance(expenses, expense_type)

    # print the updated expense amount.
    print("Expense: ", expenses[expense_type])


def update_expense(expenses, expense_type, value):
    """Updates the given expense type with the given value in the given expenses dictionary.

       Prints a friendly message if the expense type doesn't exist.  Note: Printing a friendly message means that the program should not raise an error or otherwise terminate. Simply tell the user that the requested expense type does not exist and continue the program.

       Prints the updated expense amount if it exists.

       This function doesn’t return anything.

    """
    existing_expense_amount = expenses.get(expense_type)

    # if there is no such expense type
    if existing_expense_amount == None:
        print("Sorry, that expense type does not exist.")
        return

    # update the value
    expenses[expense_type] = value

    # round the amount to 2 decimals
    round_balance(expenses, expense_type)

    # print the updated expense amount.
    print("Expense: ", expenses[expense_type])


def sort_expenses(expenses, sorting):
    """Converts the key:value pairs in the given expenses dictionary to a list of tuples and
    sorts based on the given sorting argument.

    If the sorting argument is the string ‘expense_type’, sorts the list of tuples based on the
    expense type (e.g. ‘rent’) in ascending alphabetical order,
    e.g. sorted results: ("coffee", 5), ("food", 5000), ("rent", 1000)

    Otherwise, if the sorting argument is ‘amount’, sorts the list of tuples based on the total
    expense amount (e.g. 825) in descending order,
    e.g. sorted results: ("food", 5000), ("rent", 1000), ("coffee", 5)

    Returns the list of sorted items. (Note: If the given sorting argument is not an acceptable value (e.g. ‘expense_type’ or 'amount'),
    this function does nothing except print a friendly message and return None.)
    """

    # check given sort_type
    if sorting not in ['expense_type', 'amount']:
        print("Unexpected inputs, please input ‘expense_type’ or 'amount'")
        return

    # get list of tuples
    expenses_items = list(expenses.items())

    # after converting to a list by list(), the elements is consisting of tuples,
    # which is the key:value pairs

    """If the sorting argument is the string ‘expense_type’, 
    sorts the list of tuples based on the expense type in ascending alphabetical order.
    
    If the sorting argument is the string 'amount’, 
    sorts the list of tuples based on the total expense amount in descending order.
    """

    # set reverse argument based on sorting (expense_type or amount)
    reverse = False if sorting =='expense_type' else True

    sorted_items = sorted(expenses_items, key = lambda item: item[0] if sorting == 'expense_type' else float(item[1]), reverse = reverse)

    return sorted_items


def export_expenses(expenses, expense_types, file):
    """Exports the given expense types from the given expenses dictionary to the given file.

    Do not append to the file. If the function is called again, make sure it overwrites what was previously on the
    file instead of appending to it.

    Iterates over the given expenses dictionary, filters based on the given expense types (a list of strings),
    and exports to a file.  Skips any expense type in the given list of expense types that doesn't exist.

    If the expenses argument is the dictionary {"food": 5000, "rent": 1000, "coffee": 5, "clothes": 58.92}
    and the expense_types argument is the list of strings ‘coffee, clothes, rent’, exports a file containing:
    coffee: 5
    clothes: 58.92
    rent: 1000

    If the expenses argument is the dictionary {"food": 5000, "rent": 1000, "coffee": 5, "clothes": 58.92}
    and the expense_types argument is the list of strings ‘coffee, clothes, sports’, exports a file containing:
    coffee: 5
    clothes: 58.92

    Note, the specified expense type 'sports' does not exist in the expenses dictionary, so it is ignored.

    If an item is duplicated in the given expense types, don’t worry about it, just export the data as is.
    You should not deduplicate the expense types.

    This function doesn’t return anything.
    """

    # create a list of expense amount
    expense_amounts = []

    # Iterates over the given expenses dictionary, filters based on the given expense types (a list of strings),
    for line in expense_types:
        # remove whitespace at the beginning and end of a string
        line = line.strip()
        # if there is no such expense type, skip
        if expenses.get(line) == None:
            continue
        expense_amounts.append(expenses.get(line))

    # format expenses_info_str
    expenses_info_str = ""
    for i in range(0, len(expense_types)):
        # skip /ignore non-existing expense type
        try:
            expenses_info_str += expense_types[i] + ': ' + str(expense_amounts[i]) + '\n'
        except: # if expense_types[i] is a non-existing expense type, and it has no expense_amounts. Skip
            continue

    # export expenses_info
    fout = open(file, 'w')
    fout.write(expenses_info_str)

    # close file
    fout.close()


def main():
    # import expense files and store in dictionary
    expenses = {}
    import_expenses(expenses, 'expenses.txt')
    import_expenses(expenses, 'expenses_2.txt')

    # for testing purposes, uncomment the following line
    # print(expenses)

    while True:

        # print welcome and options
        print('\nWelcome to the expense management system!  What would you like to do?')
        print('1: Get expense info')
        print('2: Add an expense')
        print('3: Deduct an expense')
        print('4: Update an expense')
        print('5: Sort expenses')
        print('6: Export expenses')
        print('0: Exit the system')

        # get user input
        option_input = input('\n')

        # try and cast to int
        try:
            option = int(option_input)

        # catch ValueError
        except ValueError:
            print("Invalid option.")

        else:

            # check options
            if option == 1:

                # get expense type and print expense info
                expense_type = input('Expense type? ')
                print(get_expense(expenses, expense_type))

            elif option == 2:

                # get expense type
                expense_type = input('Expense type? ')

                # try and get amount to add and cast to float
                try:
                    amount = float(input('Amount to add? '))

                # catch ValueError
                except ValueError:
                    print("Invalid amount.")

                else:
                    # add expense
                    add_expense(expenses, expense_type, amount)

            elif option == 3:

                # get expense type
                expense_type = input('Expense type? ')

                # try and get amount to deduct and cast to float
                try:
                    amount = float(input('Amount to deduct? '))

                # catch ValueError
                except ValueError:
                    print("Invalid amount.")

                else:
                    # deduct expense
                    deduct_expense(expenses, expense_type, amount)

            elif option == 4:

                # get expense type
                expense_type = input('Expense type? ')

                # try and get amount to update expense to
                try:
                    amount = float(input('Amount to update expense to? '))

                # catch ValueError
                except ValueError:
                    print("Invalid amount.")

                else:
                    # update expense
                    update_expense(expenses, expense_type, amount)

            elif option == 5:

                # get sort type
                sort_type = input('What type of sort? (\'expense_type\' or \'amount\') ')

                # sort expenses
                print(sort_expenses(expenses, sort_type))

            elif option == 6:

                # get filename to export to
                file_name = input('Name of file to export to?')

                # get expense types to export
                expense_types = []

                while True:
                    expense_type = input("What expense type you want to export? Input N to quit: ")
                    if expense_type == "N":
                        break

                    expense_types.append(expense_type)

                # export expenses
                export_expenses(expenses, expense_types, file_name)

            elif option == 0:

                # exit expense system
                print('Good bye!')
                break

            # corner case
            else:
                print("Invalid option.")


if __name__ == '__main__':
    main()
