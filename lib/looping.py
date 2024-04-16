#!/usr/bin/env python3

def happy_new_year():
  # code goes here!
  num = 11
  while num != 0:
    num = num - 1
    if num == 0:
      print("Happy New Year!")
    else:
      print(num)

def square_integers(int_list):
    # code goes here!
    squared = list()
    for int in int_list:
       squared_num = int * int
       squared.append(squared_num)
    return squared

def fizzbuzz():
  # code goes here!
  for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)