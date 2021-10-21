# !/usr/bin/env python3

# Created by Joshua Yeung
# Created on October 2021
# This program is to calculate the average of random number

import random


def main():
    # this function is to calculate the average of random number

    random_number = []
    total = 0

    # process
    print("starting ...")
    print("")

    for loop_counter in range(0, 10):
        some_variable = random.randint(1, 100)
        random_number.append(some_variable)

    for loop_counter_2 in range(0, len(random_number)):
        total = total + random_number[loop_counter_2]
        print("The random number is {}".format(random_number[loop_counter_2]))

    average = total / len(random_number)

    print("")
    print("The {0} ".format(average))

    print("\nDone")


if __name__ == "__main__":
    main()
