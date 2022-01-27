# Demonstrate the use of function docstrings

# """ are used as the documentation if
# it's used at the beggining of a function
def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> Doesn't really do anything special.

    Parameters:
    arg1: the first argument. Whatever you feel like passing.
    arg2: the second argument. Defaults to None. Whatever makes you happy.
    """
    print(arg1, arg2)


def main():
    # __doc__ call the documentation of a function
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
