# -*- coding: utf-8 -*-
"""Untitledsmart.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rSVmattauTHxNfUbbBfL240b8skpUbC6
"""

def binbasen(num, base):
    result = ""
    while num > 0:
        tmpbin = num % base
        result = str(tmpbin) + result
        num //= base
    return result

def divisor_sum(numbers):
    total = 0
    for num in numbers:
        divisors = []
        for i in range(1, num+1):
            if num % i == 0:
                divisors.append(i)
        total += sum(divisors)
    return total

products = []
first_values = []
while True:
  user_input = input()
  if user_input == "-1 -1":
    break
  values = user_input.split(" ")
  if len(values) == 2:
    first_values.append(values[0])
    if not 2 <= int(values[1]) <= 9:
      print("invalid base!")
      break
    else:
      sum_of_divisors = divisor_sum([int(values[0])])
      product = binbasen(sum_of_divisors, int(values[1]))
      products.append(product)

  else:
    print("Invalid input, please enter exactly two values.")
total=sum(int(num) for num in products)
print(total)