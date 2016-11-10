def prime_number(number):
    if number == 1:
        return False
    else:
        for value in range(2, int(number ** 0.5) + 1):
            if number % value == 0:
                return False
        return True
def append_prime_numbers(my_number):
    if  type(my_number) == int:

        sto_prime = []
        for item in range(2, my_number + 1):
            if prime_number(item):
                sto_prime.append(item)
        return sto_prime
    else:
        return "Numbers only"
print append_prime_numbers("str")