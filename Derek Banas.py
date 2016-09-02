# Convert miles to kilometers
'''
miles = int(input("Enter the number of miles here:  "))
kilo = miles * 1.60934
print("{} miles equals {} kilometers".format(miles, kilo))
#{} will be used to reference whatever is store in the miles and kilo variables


# enter calculation
# convert strings into integers
# use an "if" condition and output based on condition

num1, operator, num2 = input('Enter Calculation').split()
num1 = int(num1)
num2 = int(num2)
if operator =="+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator =="-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator =="*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator =="/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("Use either + - * or / next time ")


# will provide different outputs based on age
# if age is 1 -18 -> important
# 21, 50, > 65 => Important

age = eval(input("Enter age here:   "))
if (age >= 1) and (age <= 18):
    print("Important Birthday")
elif (age ==21) or (age ==50):
    print("Important Birthday")
elif not(age < 65):
    print("Important Birthday")
else:
    print("Sorry, not important"


# if age is 5 got to kindergarten
# ages 6 through 17 go to ages 1 through

age = eval(input("Enter Age here:  "))
if age < 5:
    print(" You are too young for school")
elif age == 5:
    print("go to Kindergarten")
elif (age > 5) and (age <= 17):
    grade = age - 5
    print(" Go to {} Grade".format(grade))
else:
    print("You are too old, go get a job")



# for I in {2,4,6,8,)
# for loop through list 1 to 21
# check modulus to check that the result is not = to 0

for i in range (1, 21):
    if ((i % 2) != 0):
        print("i = ", i)


#Have the user enter their investment amount and expected interest
# each year investment will increase
money = input("How much to invest :  ")
interest_rate = input("Interest Rate :  ")
# ask for the monet invested plus interest rate

# convert the value to a float
money = float(money)
# Convert value to a float and round the percentage
interest_rate = float(interest_rate) * .01
# cycle through 10 years using a loop and range 0 to 9
for i in range(10):
    money = money + (money * interest_rate)
print("Investment after 10 years : {:.2f}".format(money))


import random

rand_num = random.randrange(1,51)

i = 1

while (i != rand_num):
    i += 1

print(" The random value is : ", rand_num)



i = 1
while i <= 20:
# if the random number is even (true), this command tells python not to print
    if (i % 2) == 0:
# this tells python to increment by 1
        i += 1
# this tells python to continue on
        continue
# this tells python not to proceed past 15
    if i == 15:
        break
    print("Odd : ", i)
    i += 1



# To make a tree will need to use 1 while loop and 3 for loops

# 4 spaces : 1 Hash
# 3 space : 3 hashes
# 2 spaces : 5 hashes
# 1 space : 7 hashes
# 0 spaces : 9 hashes

# decrement space by 1 each time through the loop
# increment hashes by 2 each time through the loop
# save spaces to the stump by calculating tree height
# decrement from the tree height until it equals 0
# print stump spaces and then 1 hash

# get number of rows for the tree
tree_height = input("How tall is the tree?: ")
# convert into and integer
tree_height = int(tree_height)
# get the starting spaces for the top of the tree
spaces = tree_height - 1
# there is one hash to start that will be incremented
hashes = 1
# save stump space til later
stump_spaces = tree_height - 1
# make sure the right number of rows are printed
while tree_height != 0:
# print the spaces
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print('#', end="")
    print()
    spaces -= 1
    hashes += 2
    tree_height -= 1
for i in range(stump_spaces):
    print(' ', end="")

# print the hashes

# regular print newline after each row

# spaces decrement by 1

# hashes are ioncremented by 2 each time

# decrement tree height each time to jump out of the loop

# print the spaces for the stump

# print(' ', end="")

'''

