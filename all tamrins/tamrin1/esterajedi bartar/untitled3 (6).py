# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hzfc69uigj7I5afJnSlCpGG9iACWU_wC
"""

def x(f):
    return f+1

a=int(input("num of the first patient:"))
b=int(input("num of the last person:"))
number=0
if a<b:

  for num in range(a,b + 1):

      if num > 1:
          for i in range(2, num):
              if (num % i) == 0:
                  break

          else:
            number=x(number)
  print(f"reverse order - amount:{number}")
else:
    for num in range(b,a + 1):

      if num > 1:
          for i in range(2, num):
              if (num % i) == 0:
                  break

          else:
            number=x(number)

    print(f"main order-amount:{number}")