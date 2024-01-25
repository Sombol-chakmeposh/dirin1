# -*- coding: utf-8 -*-
"""hmm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rrch9eD8J9CgZrolbvNlK4l1ypmctbQQ
"""

def bitwise_add(a,b):
  carry=0
  result=0
  while b != 0:
    carry = a & b
    result = a ^ b
    carry = carry << 1
    a = result
    b = carry
  return result
a=int(input())
b=int(input())
c=int(input())
result=bitwise_add(a,b)
if result==c:
  print("yes")
  pass
else:
  print("no")
  pass

number = int(input('please input your number: '))
if number > 1 and number != 4:
    for i in range(2 , number//2):
        if number % i == 0:
            print('your number is not prime')
            break
    else:
        print('your number is prime')
else:
    print('your number is not prime')