"""Provide the primary functions."""
import numpy as np

def get_odds(number_list):
    odds = []
    for num in number_list:
        if num % 2 != 0:
            odds.append(num)
    
    return odds

def get_evens(number_list):
    evens = []
    for num in number_list:
        if num % 2 == 0:
            evens.append(num)
    
    return evens


def check_prime(number):
    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True


def get_primes(number_list):
    primes = []
    for num in number_list:
        if check_prime(num):
            primes.append(num)
    return primes

def look_and_say(number):
    string = str(number)
    count = 0
    old_c = string[0]
    say_string = ""
    for c in string:
        if old_c == c:
            count += 1
        else:
            say_string += str(count) + old_c
            old_c = c
            count = 1
    say_string += str(count) + c
    return int(say_string)

def get_look_and_say_sequence(inital_number, length = 10):
    look_and_say_list = [inital_number]
    for i in range(1, length):
        look_and_say_list.append(look_and_say(look_and_say_list[i-1]))
    return(look_and_say_list)

if __name__ == "__main__":
    # Do something if this file is invoked on its own
    pass
