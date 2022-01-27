# deque objects are like double-ended queues

import collections
import string


def main():
    # initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # deques support the len() function
    # str parse the value to string
    print("Item count: " + str(len(d)))

    # deques can be iterated over
    for elem in d:
        print(elem.upper(), end=",")
    print()

    # manipulate items from either end
    d.pop()
    # this will pop the element at th beggining
    d.popleft()
    d.append(2)
    # this will add it at the begging
    d.appendleft(1)
    print(d)

    # rotate the deque
    print(d)
    # rotate will move then spaces inside the deck
    # when you rotate the value from the end will
    # go to the begging
    d.rotate(2)
    print(d)


if __name__ == "__main__":
    main()
