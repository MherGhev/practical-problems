import math
import time

# 1
def ex1():
    print("Mher, Aygektsi 47")

# 2
def ex2():
    name = input("What is Your name? ")
    print(f"Hi {name}!")

# 3
def ex3():
    length = int(input("Input the length in meters: "))
    width = int(input("Input the width in meters: "))
    print(f"The are of the room with length {length} m. and width {width} is {length*width} square meters.")

# 4
def ex4():
    length = int(input("Input the length in feet: "))
    width = int(input("Input the width in feet: "))
    print(f"Area in acres is {width * length / 43560}")

# 5
def ex5():
    smallBottles = int(input("How many bottles with volume 1 liter or below? "))
    bigBottles = int(input("How many bottles with volume above 1 liter? "))
    print(f"The price is ${(0.10 * smallBottles + 0.25 * bigBottles):.2f}")

# 6
def ex6():
    cost = float(input("Input the cost: "))
    print(f"Tip: ${round(cost*0.18, 2)}")
    print(f"Tax: ${round(cost * 1.18 * 0.2, 2)}")
    print(f"Total: ${round(cost * 1.18 * 1.2, 2)}")

# 7
def ex7():
    num = int(input("Input a number: "))
    def sum_of_nums(n):
        return n if n == 1 else n + sum_of_nums(n-1)
    print(f"The sum of all of the previous numbers is {sum_of_nums(num)}")

# 8
def ex8():
    souvenirs = int(input("Number of souvenirs: "))
    others = int(input("Number of other things: "))
    print(f"The total weight of your purchase is: {souvenirs * 75 + others * 112} grams.")

# 9
def ex9():
    def calculatePercentage(money, year, percent):
        percent = percent/100 + 1
        result = money
        i = 0
        while i < year:
            result *= percent
            i += 1
        return round(result, 2)

    my_money = float(input("Dollars in bank account: "))
    print(f"First year: ${calculatePercentage(my_money, 1, 4)}")
    print(f"Second year: {calculatePercentage(my_money, 2, 4)}")
    print(f"Third year: {calculatePercentage(my_money, 3, 4)}")

# 10
def ex10():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print(f"Sum: {num1+num2}.")
    print(f"Difference: {num1-num2}.")
    if not num2 == 0:
        print(f"Ratio: {num1/num2}.")
        print(f"Whole part: {num1//num2}")
        print(f"Remainder: {num1%num2}")
    else:
        print("Cannot divide by zero.")

    if num1 > 0:
        print(math.log(num1, 10))

# 11
def ex11():
    mpg = float(input("Miles per gallon: "))
    lpk = 1/(1.609 * mpg/378.54117)
    print(f"Liters per 100km: {round(lpk, 3)}")

# 12
def ex12():
    feet = int(input("How many feet: "))
    inches = int(input("How many inches: "))
    print(f"{(inches + (feet * 12)) * 2.54} in centimeters.")

# 13
def ex13():
    feet = float(input("How many feet: "))
    print("That is equivalent of:")
    print(f"{feet * 12} inches.")
    print(f"{feet * 0.33} yards.")
    print(f"{round(feet * 0.000189394, 3)} miles.")

# 14
def ex14():
    r = float(input("Radius: "))
    print(f"{3.14 * r * r}: Area of circle with radius {r}")
    print(f"{round((4 * 3.14 * (r**3))/3, 2)}: Volume of a globe with radius {r}")

# 15
def ex15():
    r = float(input("Radius of the cylinder: "))
    h = float(input("Height of the cylinder: "))
    print(f"Volume of the cylinder is {round(h * 3.14 * r * r)}")

# 16
def ex16():
    h = float(input("Release height in meters: "))
    print(f"The final velosity will be: {math.sqrt(2 * 9.8 * h)} m/s")

# 17
def ex17():
    base = float(input("Input base: "))
    height = float(input("Input height: "))
    print(f"Area od the triangle is: {base*height/2}")

# 18
def ex18():
    s1 = float(input("Side 1: "))
    s2 = float(input("Side 2: "))
    s3 = float(input("Side 3: "))

    s = (s1 + s2 + s3)/2
    print(f"Area of the triangle: {math.sqrt(s * (s-s1) * (s-s2) * (s-s3))}")


# 19
def ex19():
    days = int(input("Days: "))
    hours = int(input("Hours: "))
    minutes = int(input("Minutes: "))
    seconds = int(input("Seconds: "))

    print(f"Total seconds: {days* 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds}")

# 20
def ex20():
    print(time.asctime())


# 21

def formatString(str):
    result = ""
    for i in range(len(str)):
        if i == 0:
            result += str[i].upper()
        else:
            result += str[i].lower()
    return result

def ex21():
    good_answer = False
    month30 = ["September", "April", "June", "November"]
    month31 = ["January", "March", "May", "July", "August", "October", "December"]

    while not good_answer:
        month = input("Input the name of the month: ")

        month = formatString(month)

        if month in month30:
            print(f"{month} has 30 days.")        
            good_answer = True
        elif month in month31:
            print(f"{month} has 31 days.")
            good_answer = True
        elif month == "February":
            print(f"{month} has 28 or 29 days.")
            good_answer = True
        else:
            print("Please enter a valid name of a month.")


# 22
def ex22():
    vowels = ["a", "e", "i", "o", "u"]
    good_answer = False
    while not good_answer:
        letter = input("Input a letter: ")
        letter = letter.lower()
        if not len(letter) == 1:
            print("Please input one letter.")
        elif letter in vowels:
            print(f"{letter} is a vowel.")
            good_answer = True
        elif letter == "y":
            print("y can be both a vowel and a consonant")
            good_answer = True
        else:
            print(f"{letter} is a consonant.")
            good_answer = True

# 23
def ex23():
    winter = ["December", "January", "February"]
    spring = ["March", "April", "May"]
    summer = ["June", "July", "August"]
    fall = ["September", "Octpber", "November"]

    month30 = ["September", "April", "June", "November"]
    month31 = ["January", "March", "May", "July", "August", "October", "December"]



    good_answer = False
    while not good_answer:
        month = input("Input the month: ")
        day = int(input("Input the day: "))
        month = formatString(month)
        if ((month in month30 and day <= 30) or (month in month31 and day <= 31) or (month == "February" and day <= 29)):
            if month in winter:
                print(f"{month} {day} is in winter.")
                good_answer = True
            elif month in spring:
                print(f"{month} {day} is in spring.")
                good_answer = True
            elif month in summer:
                print(f"{month} {day} is in summer.")
                good_answer = True
            elif month in fall:
                print(f"{month} {day} is in winter.")
                good_answer = True
        else:
            print("Please enter a valid date.")
            
# 24
def ex24():
    finished = False
    list_of_nums = []
    while not finished:
        num = int(input("Enter a number: "))
        if num == 0:
            if len(list_of_nums) ==  0:
                raise Exception("No numbers inputted.")
            finished = True
        else:
            list_of_nums.append(num)

    average = sum(list_of_nums) / len(list_of_nums)
    print(f"The mean of the entered numbers is {average}")

# 25
def ex25():
    def celToFah(cel):
        return cel* 1.8 + 32
    print("C - F")
    for i in range (0, 101, 10):
        print(f"{i} - {celToFah(i)}")

# 26
def ex26():
    for i in range(1, 101):
        if i%3 == 0 and i%5 == 0:
            print("Fizz-Buzz")
        elif i%5 == 0:
            print("Buzz")
        elif i%3 == 0:
            print("Fizz")
        else:
            print(i)

# ex1()
# ex2()
# ex3()
# ex4()
# ex5()
# ex6()
# ex7()
# ex8()
# ex9()
# ex10()
# ex11()
# ex12()
# ex13()
# ex14()
# ex15()
# ex16()
# ex17()
# ex18()
# ex19()
# ex20()
# ex21()
# ex22()
# ex23()
# ex24()
# ex25()
# ex26()