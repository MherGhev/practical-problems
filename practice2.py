from math import fabs
import random


def ex1():
    finished = False
    lst_of_words = []
    while not finished:
        word = input("Enter a word: ")
        if word == "":
            finished = True
        else:
            lst_of_words.append(word)

    result = []
    for w in lst_of_words:
        if not w in result:
            result.append(w)
            print(w)

# ex1()

def ex2(number):
    return [i for i in range(1, number) if number%i == 0]

# print(ex2(60))

def ex3(number):
    return sum(ex2(number)) == number

# print(ex3(28))
# print(ex3(29))

def my_zip(data1, data2):
    if not len(data1) == len(data2):
        raise Exception("The lengths of the lists must be equal.")

    result = [None] * len(data1)

    for i in range(len(data1)):
        result[i] = [data1[i], data2[i]]
    return result

# print(my_zip([1,2,3,4],[10,20,30,40]))

def is_palindrome(string):
    signs = '`~,.;:\|"\'!@#$%^&*()<>\{\}[]?'
    clean_string = ""
    for l in string:
        if not l in signs:
            clean_string += l
    
    lst = clean_string.split(" ")

    for i in range((len(lst)//2) + 1):
        lst[i] = lst[i].lower()
        if not lst[i] == lst[len(lst) - i - 1]:
            return False

    return True

# print(is_palindrome("Herb the sage eats sage, the herb"))
# print(is_palindrome("Information school graduate seeks graduate school information"))
# print(is_palindrome("This is not a palindrome sentence!"))

def ex6():
    finished = False
    list_of_num = []
    while not finished:
        number = input("Enter a number: ")
        if not number == "":
            number = int(number)
            list_of_num.append(number)
        else:
            finished = True
    
    average = sum(list_of_num)/ len(list_of_num)

    greater_than_ave = []
    smaller_than_ave = []
    average_count = 0
    for n in list_of_num:
        if n > average:
            greater_than_ave.append(n)
        elif n < average:
            smaller_than_ave.append(n)
        else:
            average_count += 1

    print(f"The average is {average}")
    print(f"List of numbers below average: {smaller_than_ave}")
    print(f"Number of numbers equal to the average: {average_count}")
    print(f"List of numbers above average: {greater_than_ave}")

# ex6()

def ex7():
    list_of_numbers = []
    t = 0
    while t < 6:
        rand_n = random.randint(1, 49)
        if not rand_n in list_of_numbers:
            list_of_numbers.append(rand_n)
            t += 1
    list_of_numbers.sort()
    return list_of_numbers

# print(ex7())

def ex8(my_list):
    result = [None] * len(my_list)
    result[:] = my_list[:]
    
    result.sort()
    if my_list == result:
        return True
    result.sort(reverse=True)
    if my_list == result:
        return True
    
    return False

# print(ex8([4,3,2,1]))
# print(ex8([1,2,3,4]))
# print(ex8([1,2,3,2,1]))

def is_sublist(longer, shorter):
    list1 = []
    for i in range(len(longer) - len(shorter)+1):
        list2 = []
        for j in range(len(shorter)):
            list2.append(longer[i+j])
        list1.append(list2)
    return shorter in list1


long_list = [1, 2, 3, 4, 5]
short_list = [1, 2, 3]
print(is_sublist(long_list, short_list))