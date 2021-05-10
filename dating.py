#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program lets the user see if they can date a grandchild

import random
import string


def main():
    # This function determines the user's eligibility as a potential partner

    # Input
    age_as_string = str(input("Enter your age: "))

    # Process and Output
    try:
        age_as_integer = int(age_as_string)
        if age_as_integer > 25 and age_as_integer < 40:
            print("\nYou can date my grandchild!")
        elif age_as_integer <= 25:
            print("\nYou are too young!")
        else:
            print("\nYou are too old!")
    except Exception:
        print("\n{} is not a valid age!".format(age_as_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
