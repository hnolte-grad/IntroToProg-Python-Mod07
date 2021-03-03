# ----------------------------------------------------------------#
# title: Assignment 07
# description: tutorial program that educates the user on pickling
#           and error handling in Python
# change log:
# Hannah Clayton,23feb2021, created file
#                02Mar2021, finished code
# -----------------------------------------------------------------#

# import functions
import colorama
import pickle as pkl

# define variables
gFileName = "PickleDoc.txt"                                     # the name of pickled data file
lstTable = []                                                   # for storing data to be pickled
gTask = None                                                    # user task input
gPriority = None                                                # user priority input
gChoice = None                                                  # user menu choice
gNumber = None                                                  # user input in error handling tut

# define classes and functions
class P:                                                        # processing data
    @staticmethod
    def err_py_msg(number):                                     # displays python's usual error message (gNumber)
        from colorama import Fore, Style
        try:
            int(number)
        except ValueError as e:
            print('Python generated error information:\n ',
                  Fore.RED + str(e),
                  type(e),
                  e.__doc__,
                  e.__str__(),
                  Style.RESET_ALL)
        return()

    @staticmethod
    def err_cust_msg(number):                                   # displays custom error message (gNumber)
        from colorama import Fore, Style
        try:
            int(number)
        except ValueError:
            print(Fore.RED + 'Error! You entered characters instead of a number, please try again.',
                  Style.RESET_ALL)
            print('-' * 100)
        return()

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):          # (gTask, gPriority, and lstTable) global arg in main
        dicRow = {'Task': task.lower(), 'Priority': priority}
        list_of_rows.append(dicRow)
        return list_of_rows, 'Success'

    @staticmethod
    def pkl_write(file_name, list_of_rows):                      # writes to file (gFileName, lstTable)
        with open(file_name, 'wb') as f:
            pkl.dump(list_of_rows, f)
        f.close()

    @staticmethod
    def pkl_load(file_name, list_of_rows):                      # loads from file (gFileName, lstTable)
        try:
            while True:
                yield pkl.load(file_name)
        except EOFError:
            pass
        list_of_rows.clear()  # clear current data
        with open(file_name, "rb") as f:
            for line in f:
                list_of_rows = pkl.load(f, encoding='bytes')
                task, priority = line.split()  # you can set two variables at a time
                row = {"Task": task.strip(), "Priority": priority.strip()}
                list_of_rows.append(row)
        f.close()
        return list_of_rows, 'Success'


class IO:                                                        # input/output class
    @staticmethod
    def err_handle_interface():                                  # error handling interface pt1
        from colorama import Fore, Style
        print('-'*100)
        print(Fore.CYAN,
              '''
              \tError Handling Tutorial:\n
              This is how error handling works.
              I am going to ask for a number.
              Instead of giving me a number, try giving me a word instead.\n
              ''',
              Style.RESET_ALL)
        print('-'*100)
        number = input(' Enter a number between 1- 10: ')
        return number

    @staticmethod
    def err_handle_interface2():                                # error handling interface pt2
        from colorama import Fore, Style
        print('-' * 100)
        print(Fore.CYAN,
              '''
              Now normally this would result in an error with the above information,
                and your program would close, because you input a string when Py was 
                expecting an integer.
              But because I have 'captured' the error, 
                I can now change the information that the user receives when the error comes up.
              Lets try it again...
              [Please remember to insert a word instead of a number]
              ''',
              Style.RESET_ALL)
        print('-' * 100)
        number = input('\nEnter a number between 1- 10: ')
        return number

    @staticmethod
    def err_handle_interface3():                                  # error handling interface pt3
        from colorama import Fore, Style
        print('-' * 100)
        print(Fore.CYAN,
              '''As you can see, error handling can be useful in interacting with a user,
              \tas traditional python error handling can be difficult to understand.''',
              Style.RESET_ALL)
        print('-' * 100)
        input('\nPress [Enter] to return to main menu: ')
        return ()

    @staticmethod
    def input_new_task_and_priority():                              # captures task and priority
        task = input('Enter a task: ')
        priority = input(str('Enter a priority[1-5]: '))
        return task, priority

    @staticmethod
    def pick_menu():                                                # displays menu
        from colorama import Fore, Style
        print('-' * 100)
        print(Fore.CYAN,
              '''
              Welcome to this week's tutorial on pickling and error handling.
              Menu of Options
              1) Lets 'pickle'.
              2) Handle all these errors
              3) Exit tutorial
              ''',
              Style.RESET_ALL)
        print('-' * 100)
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():                                         # captures user input for menu nav
        choice = str(input("Which option would you like to perform? [1 or 2] - ")).strip()
        print()
        return choice

    @staticmethod
    def opt_msg(opt_msg=''):                                         # for varying messages thru main
        from colorama import Fore, Style
        print('-' * 100)
        print(Fore.CYAN,
              opt_msg,
              Style.RESET_ALL)
        print('-' * 100)
        input('[Press Enter to Cont]')
        return

    @staticmethod
    def pkl_interface1():                                             # pickling tut part1
        from colorama import Fore, Style
        print('-' * 100)
        print(Fore.CYAN,
              '''
            Pickling is a method used by Python to write information to a file in binary format,
                instead of regular text.
            Storing in a binary format can reduce file size and be used cross-platforms and languages. 
            To show you how pickling works, I am going to use a program from last week's assignment 
                involving a to-do list.
            Please follow the prompts.''',
              Style.RESET_ALL)
        print('-' * 100)

    @staticmethod
    def pkl_interface2():                                              # pickling tut part2
        from colorama import Fore, Style
        print('-' * 100)
        print(Fore.CYAN,
              '''
            The data you put in has now been writen to a file labeled 'PickleDoc.txt
            The document should contain odd data that looks something like this:
            '€•#       ]”}”(ŒTask”Œhw”ŒPriority”Œ1”ua.'
            You can write to a file in binary format using the 'pickle.dump' method.
            ***NOTE: Document will not populate in pycharm until program ends***
            ''',
              Style.RESET_ALL)

    @staticmethod
    def pkl_interface3(list_of_rows):                                   # pickling tut part3
        from colorama import Fore, Style
        print('-' * 100)
        print(Fore.CYAN,
              '''
        To load pickled data from a file I use the 'pickle.load' method.
        The code I've written loops through the data in the file, 
        loading it back into the original data table.
        Here's your data:
            ''',
              Style.RESET_ALL)
        print(list_of_rows)

# Main
while (True):
    IO.pick_menu()
    gChoice = IO.input_menu_choice()

    if gChoice.strip() == '1':                                      # pickling tut
        IO.pkl_interface1()
        gTask, gPriority = IO.input_new_task_and_priority()
        P.add_data_to_list(gTask, gPriority, lstTable)
        IO.opt_msg("I've added the tasks you input to a table, next we'll save them.")
        P.pkl_write(gFileName, lstTable)
        IO.pkl_interface2()
        IO.opt_msg("Next we'll look at loading data from a pickled file.")
        P.pkl_load(gFileName, lstTable)
        IO.pkl_interface3(lstTable)
        IO.opt_msg("That's all for pickling.")

    elif gChoice == '2':                                            # error handling tut
        gNumber=IO.err_handle_interface()
        P.err_py_msg(gNumber)
        gNumber = IO.err_handle_interface2()
        P.err_cust_msg(gNumber)
        IO.err_handle_interface3()

    elif gChoice == '3':
        print('Goodbye!')
        break

    else:
        IO.opt_msg('Invalid Menu Choice, try again.')

