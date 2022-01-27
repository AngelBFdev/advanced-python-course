# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
# * avoids to access to the last parameter
def myFunction(arg1, arg2, *, suppressExceptions=False):
    print(arg1, arg2, suppressExceptions)


def main():
    # try to call the function without the keyword
    # this gives you an error since the
    # last parameter is a keyword
    # myFunction(1, 2, True)
    myFunction(1, 2, suppressExceptions=True)


if __name__ == "__main__":
    main()
