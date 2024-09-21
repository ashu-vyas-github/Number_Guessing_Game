#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: ashutosh

Command-line based number guessing game using infinite while loop.

A command-line based number guessing game for killing time.
It uses the random module to guess a number by computer. The user guesses a number in a range (eg: 1 to 100).
The infinite while loop runs using a flag which is set to True when user guesses the number correctly.
For wrong guesses, the user is alerted if the guessed number is higher or lower than the random module generated
number. This helps to converge to an outcome of success, otherwise the game becomes infinitely long to finish.
For invalid inputs, such as alphabet or special characters, the user is alerted about the wrong input and is asked
to input the number only in the provided range correctly.
"""
import random


class NotInRangeError(ValueError):
    """
    NotInRangeError Exception to check whether the number is within the provided range or not.

    This exception extends ValueError. It accepts an integer as input. Checks the input number with provided
    upper and lower limits in the main program. If the number is out of the range, this exception is raised.

    Parameters
    ----------
    ValueError : built-in exception class.
        This is the built-in class from python standard library. It is used as a baseclass for this new exception.
    """


def verify_input(
    lower_range=1, upper_range=100, num_guesses=0, input_correct_flag=False
):
    """
    verify_input Verify the input provided by the user is a number, and in the range.

    Checking and verifying the input provided by user is a very important step for the correct working of the game.

    Parameters
    ----------
    lower_range : int, optional
        Lower range to compare the input number, by default 1.
    upper_range : int, optional
        Upper range to compare the input number, by default 100.
    num_guesses : int, optional
        Number of guesses, trials, asking user for input, by default 0.
    input_correct_flag : bool, optional
        Flag to check whether the input from user was an integer or not.
        It is True when the input is an integer value and is in within range, by default False.

    Returns
    -------
    user_input : int
        The input integer number provided by the user.
    num_guesses : int, optional
        Number of guesses, trials, asking user for input.
    input_correct_flag : bool, optional
        Flag with True value to signify the input from user was an integer, False otherwise.

    Raises
    ------
    NotInRangeError
        User-defined exception to tackle the input number being within provided range. Raised when out-of-range.
    ValueError
        If the input number is not an integer type.
    """
    user_input = input(
        f"Guess an integer number between {lower_range} to {upper_range}: "
    )
    try:
        user_input = int(user_input)
        if (user_input < lower_range) or (user_input > upper_range):
            raise NotInRangeError
        input_correct_flag = True
        num_guesses += 1
    except NotInRangeError:
        print(
            f'Number "{user_input}" is not in the provided range {lower_range} to {upper_range}.'
        )
        input_correct_flag = False
        num_guesses += 1
    except ValueError:
        print(f'Only integer numbers are acceptable. "{user_input}" is not an integer.')
        input_correct_flag = False
        num_guesses += 1

    return user_input, num_guesses, input_correct_flag


def compare_guesses(user_input, computer_number, num_guesses, guess_flag):
    """
    compare_guesses Comparing user provided guess for an integer number and computer generated random number.

    The user provides a guess for an integer number within a range. This guess is then compared with a computer-
    generated random integer from the same range. The else-block acts as catch-all case for any invalid inputs.
    A flag is set to True for the correct guess, while set to False for wrong, invalid guesses.
    The function returns this flag to the main runtime procedure to be used in the while loop conditional check.

    Parameters
    ----------
    user_input : int
        The input integer number provided by the user.
    computer_number : int
        The integer number generated by the random module.
    num_guesses : int
        Number of guesses, trials, asking user for input.
    guess_flag : bool
        Flag, set to True, when user guesses the number correctly, and False otherwise.

    Returns
    -------
    guess_flag : bool
        Flag, set to True, when user guesses the number correctly, and False otherwise. It is used by main() procedure.
    """

    if user_input == computer_number:
        print(f"Correct guess! It took you {num_guesses} tries!")
        guess_flag = True
    elif user_input < computer_number:
        print("Too low! Try again.")
        guess_flag = False
    elif user_input > computer_number:
        print("Too high! Try again.")
        guess_flag = False
    else:
        print("Invalid input. Only provide numbers.")
        guess_flag = False
    return guess_flag


# RUNTIME PROCEDURE
def main():
    """
    main Main runtime procedure to execute upon launching the app from command-line or terminal.

    Returns
    -------
    int
        Returns 0 on successful execution of main(), similar to exit code 0, to make function return value.
    """
    start_num = 1
    end_num = 100
    computer_number = random.randint(start_num, end_num)
    num_guesses = 0
    guess_flag = False
    while guess_flag is False:
        input_correct_flag = False
        while input_correct_flag is False:
            user_input, num_guesses, input_correct_flag = verify_input(
                lower_range=start_num,
                upper_range=end_num,
                num_guesses=num_guesses,
                input_correct_flag=input_correct_flag,
            )
        guess_flag = compare_guesses(
            user_input=user_input,
            computer_number=computer_number,
            num_guesses=num_guesses,
            guess_flag=guess_flag,
        )
    print("\nDone\n")

    return 0


if __name__ == "__main__":
    main()
