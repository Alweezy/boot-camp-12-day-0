# boot-camp-12-day-0
A function to generate prime numbers from 0 to n.

##################################################
This program consits of two functions:
The first function specifies how a prime number can be calculated.This is the function that dictates the amount o time that will be used to evaluate if a number is a prime number.

It really cuts down the time needed to evaluate if a number is prime by using the __trial division__,a routine consists of dividing a number x by each integer y that is greater than 1 and less than or equal to the square root of x. If the result of any of these divisions is an integer, then n is not a prime, otherwise it is.

The second function just evaluates if the input in question is an integer before calling the first function to compute the prime numbers then put them into a list.
