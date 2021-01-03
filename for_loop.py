# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program is a loop a for loop


def main():
    # this function uses a for loop

    # input
    positive_integer = input("Enter how many times to calculates the square: ")

    # process and output
    try:
        positive_integer = int(positive_integer)
        if positive_integer > 0:
            for counter in range(positive_integer + 1):
                print("{0}² = {1}.".format(counter, (counter*counter)))
        else:
            print("sorry, this was not a posetive integer")
    except Exception:
        print("sorry, this was not a posetive integer")


if __name__ == "__main__":
    main()
