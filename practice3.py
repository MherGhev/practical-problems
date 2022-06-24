import math, random

def ex1(n):
    result = 0
    while n > 0:
        result *=10
        result += n % 10
        n = n//10
        
    return result

def ex2(tup):
    result = 0
    for el in tup:
        result *= 10
        result += el
    return result

def sum_of_max_min(data):
    max = data[0]
    min = data[0]

    for el in data:
        if el > max:
            max = el
        elif el < min:
            min = el
    return max + min

def ex4(my_list):
    for i in range(len(my_list)):
        if my_list[i]%2 == 0:
            print(i)
    
def ex5(word):
    i = len(word) - 1
    result = ""
    while i >= 0:
        result += word[i]
        i -= 1
    return result

def is_prime(number):
    for n in range(2, math.floor(math.sqrt(number)) + 1):
        if number % n == 0:
            return False
    return True

def smallest_prime(n):
    if n <= 0:
        return 2
    n += 1
    while True:
        if is_prime(n):
            return n
        n += 1

def get_median(data):
    data.sort()
    if len(data) % 2 == 0:
        return (data[(len(data)//2) - 1] + data[len(data)//2]) / 2
    return data[len(data)//2]

def is_leap(year):
    if year%4 == 0:
        if year%100 ==0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def ex8(month, year):
    if month <0 or month > 12:
        raise Exception("No such month.")

    month30 = [9, 4, 6, 11]
    month31 = [1, 3, 5, 7, 8, 10, 12]
    if month in month30:
        return 30
    elif month in month31:
        return 31
    if is_leap(year):
        return 29
    return 28

    
def random_psswd(n):
    if n <= 0:
        raise Exception("Not a proper password length.")
    
    password = ""
    while n > 0:
        rand_symbol = random.randint(33, 126)
        password += chr(rand_symbol)
        n -= 1
    return password

def same_parity(n, *args):
    result = []
    for el in args:
        if el%n == 0:
            result.append(el)
    return result

# print(ex1(123))
# print(ex2((1,2,3,4)))
# print(sum_of_max_min([1, 2, 3, 4, 5]))
# ex4([1, 2, 3, 4, 5])
# word = input("Enter a word: ")
# print(ex5(word))
# print(smallest_prime(0))
# print(get_median([2, 1, 3, 4, 5, 6]))
# print(ex8(2, 2020))
# print(ex8(2, 2021))
# print(random_psswd(10))
# print(same_parity(4, 2, 10, 20, 40, 32))

