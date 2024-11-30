
# Basic Function Questions

# 1. Write a function to calculate the area of a circle given its radius.
# def calculate_area_of_circle(radius):
#     area = 3.14 * radius ** 2
#     return area
# radius = 5
# print("area is: ", calculate_area_of_circle(radius))

# 2. Create a function that takes two numbers and returns their sum.

# def add_numbers(num1, num2):
#     return num1 + num2
# result = add_numbers(5, 3)
# print("The sum is:", result)

# simple program 
# def sum_of_two_numbers(add):
    #     resul_sum = num1 + num2
#     return resul_sum
# num1 = 5
# num2 = 6
# print("The sum is: ", sum_of_two_numbers())


# def my_function():
#     num1 = 5
#     num2 = 4
#     sum = num1 + num2
#     print(sum)
# my_function()

# 3. Write a function to find the factorial of a number using recursion.

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(5)) 

# 4. Write a function that takes a string and returns it reversed.
# def string(s):
#     return s[::-1]
# result = string("Hello")
# print(result)

# def string():
#     str = "Book"
#     print(str[::-1])
# string()

# 5. Create a function to check if a given number is prime.
# def check_prime(num):
#     if num % 2 == 0:
#         return 
    

# print("Not a prime:", check_prime(7))
# print("Prime: ", check_prime(8))




# def check_prime():
#     num = int(input("Enter a number: "))
# for i in range(2, num):
#     if num  % i == 0:
#         print("Number is not a prime: ")
#         break
# else:
#     print("Number is prime: ")
# check_prime()

# 6. Write a function to count the vowels in a given string.

# str = input("Enter the string: ")
# count = 0
# list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# for char in str:
#     if char in list:
#         count = count + 1
# print(count)



                                        # Intermediate Function Questions

# 1. Create a function that takes a list of numbers and returns the largest number.


# a = int(input("Enter 1st no: "))
# b = int(input("Enter 2nd no: "))
# c = int(input("Enter 3rd no: "))
 
# if a > b and a>c:
#     print("A is Greater: ")
# elif b>a and b>c:
#     print("B is Greater: ")
# else:
    
#     print("C is Greater: ")

# 2. Write a function to find the nth Fibonacci number using recursion.
# def fibo(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     return (fibo(n-2)+fibo(n-1))
# n = int(input("Enter number of terms: "))
# for i in range(1, n+1):
#     print(fibo(i))

# 3. Write a function to check whether a string is a palindrome.


# num = int(input("Enter a number: "))
# temp = num 
# sum = 0
# while num>0:
#     r =num%10
#     sum = sum*10+r
#     num = num//10
# if temp==sum:
#     print("Number is Palindrome: ")
# else:
#     print("Number is Not Palindrome: ")

# 4. Create a function that takes a list of integers and returns the sum of all even numbers.
# def list(list):
#     list = [1, 2, 4, 5, 75, 75, 74, 43, 54]
#     sum = 0
#     for i in list:
#         sum = sum + i
#     print("Sum of list is: ", sum)
# list(list)

# 5. Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# if num1 > num2:
#     print("Numer one is greater: ")
# else:
#     print("Number two is greater: ")

# 6. Create a function that accepts a dictionary and returns the key with the highest value.
# data = {'x':200, "y":300,"z":100}
# val = max(data, key= data.get)
# print(val)

          # Advanced Function Questions
# 1. Write a function that calculates the power of a number without using the ** operator.
# 2. Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa.
# celsius = 34
# fahrenheit = (celsius * 1.8) + 32
# print(" %.2f celsius = %.2f Fahrenheit" %( celsius, fahrenheit ))

# 3. Write a function to flatten a nested list.
# list1 = [[1], [2,3], [4,5, 6, 7]]
# result = [num for sublist in list1 for num in sublist]
# print("Original list: ", list1)
# print("Result list: ", result)

# 4. Create a function to check if two strings are anagrams.
# anagrams mean same words both lines.
# word1 = "Listen"
# word2 = "Listen"
# sorted_word1 = sorted(word1)
# sorted_word2 = sorted(word2)
# is_anagram = sorted_word1 == sorted_word2
# if is_anagram:
#     print("The words are anagrams: ")
# else:
#     print("The words are not anagrams: ")

# 5. Write a function that takes a list and removes all duplicate elements.
# a = [10, 20,30,40,30,10,20,50,60,50]
# dup_items = set()
# uniq_items = []
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)
#     print(dup_items)

# 6. Create a function that takes a string and counts the frequency of each character.

print(bool(""))