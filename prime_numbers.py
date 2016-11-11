def prime_number(number):
    if number is 1:
      return False
    else:
        for value in range(2, int(number ** 0.5) + 1):
          if number % value is 0:
              return False
        return True

def append_prime_numbers(my_number):
   sto_prime = []
   if not isinstance(my_number, int) or type(my_number) is bool:
      return "Operation cannot allow " + str(type(my_number)) + ", integers only."
   elif my_number <= 0:
      return "Prime numbers exist only for positive integers"
   elif isinstance(my_number, int):
      for item in range(2, my_number + 1):
        if prime_number(item):
          sto_prime.append(item)
      return sto_prime

print append_prime_numbers(False)