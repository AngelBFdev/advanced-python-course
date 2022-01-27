# Demonstrate the usage of defaultdict objects

from collections import defaultdict


def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    # this will create a default value for each
    # new key, in this case with int and will start
    # at 0
    fruitCounter = defaultdict(int)

    # Count the elements in the list
    # for each element in fruits array
    for fruit in fruits:
        # save the value of a key as the number
        # key: apple, value: 1
        # if it's the same name will access
        # to that value and increment it
        # fruitCounter[apple] += 1
        # key: apple, value: 2
        fruitCounter[fruit] += 1

    # print the result
    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))


if __name__ == "__main__":
    main()
