#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: October 2022
# This program calculates the sum of two numbers
#    with user input

import math


def main():
    # this function calculates sum of two number

    # input
    integer_one = int(input("Enter integer one: "))
    integer_two = int(input("Enter integer two: "))

    # process
    sum = integer_one + integer_two

    # output
    print(
        "\nSum is {0:,} + {1:,} = {2:,}.".format(integer_one, integer_two, sum))


    print(
        "\nDone.")


if __name__ == "__main__":
    main()
