FILEPATH = "todos.txt" # No need for this here - filepath is called from main
# in function def arguments
# default parameter (filepath). No need for argument down at function call


def get_todos(filepath=FILEPATH):
    #Read a text file and return the list of todo items
    with open(filepath, "r") as file_local:  # opens "todos.txt" in read mode
        # read all from file_local and pass them to todos_local as string
        todos_local = file_local.readlines()
    return todos_local


# todos_arg is a local variable argument, todos in main App1 is a global variable
# non default parameter (todos_arg) must come before default parameters (filepath)
def write_todos(todos_arg, filepath = FILEPATH):
    #Write the todos items into the text file
    with open(FILEPATH, "w") as file:
        file.writelines(todos_arg)  # write the argument to file and close file


print("I am writing to you from the app1_functions script!!")

# this is a variable (__name__). When running main (Main.py) indirectly
# it prints the name of this module i.e. app1_function
# but when you run this script (app1_function) it prints __main__
# use this when running this script directly to test functions above before
print(__name__)
# calling them from main program
if __name__ == "__main__":  # if statement prevents "Hello" and get_todos
    # from printing in main when this module is called
    print("Hello")
    print(get_todos(filepath = FILEPATH))
