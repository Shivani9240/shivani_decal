#1. Oski Stole Your Power
#Oski hacked your computer and you can no longer use x**y or pow(x, y). Find a
#different way (by writing a function) that can compute x raised to the power of y.

def computePower(x, y):
    ans = 1
    for i in range(y):
        ans *= x
    return ans
computePower(2, 3)
print(computePower(2, 3))

#2. What Should I Wear?
#You are trying to decide what to wear to the Python DeCal lecture, but you are
#only concerned about the day’s lowest and highest temperatures. Write a function
#that takes in a list as input and returns a tuple with the min and max as two values.

def temperatureRange(readings):
  Min = min(readings)
  Max = max(readings)
  return (Min,Max)
temperatureRange([15, 14, 17, 20, 23, 28, 20])
print(temperatureRange([15, 14, 17, 20, 23, 28, 20]))

#3. Check if its the Weekend
#All your classes have assigned problem sets due next week, and you want to
#check if it’s the weekend so you have time to work on them. Write a function
#that takes a day of the week (represented as an integer, where 1 = Monday, 2
#= Tuesday, etc) and returns True if its a weekend and False if otherwise.

def isWeekend(day):
  if day == 6 or day == 7:
    return True
  else:
    return False
isWeekend(6)
print(isWeekend(6))

#4. Fuel Efficiency Calculator
#The Python DeCal wants to take a trip to the Lick Observatory ( San Jose, CA)
# and they want to pick the best car. Write a function that takes the distance
#traveled (in miles) and the amount of fuel consumed (in gallons) as input and
#returns the fuel efficiency.

def fuel_efficiency(distance, fuel):
  efficiency = int(distance)/float(fuel)
  ans = round(efficiency,2)
  return ans
fuel_efficiency(70, 21.5)
print(fuel_efficiency(70, 21.5))

#5. Secret Code
#Write a function that takes an integer as input and moves its last digit to
#the front of the number. You may NOT convert the input to a string. Hint: Try
#modulus (%) and floor division. (\\) to solve this problem.

def decodeNumbers(n):
  Last_digit = n % 10
  Without_last_digit = n // 10
  return int(str(Last_digit) + str(Without_last_digit))
decodeNumbers(12345)
print(decodeNumbers(12345))

#6.1 For Loops
#Write two functions to manually find the minimum and maximum values in a
#list of numbers with for loops.

#Minimum
def find_min_with_for_loop(nums):
  Min = nums[0]
  for i in nums:
    if i < Min:
      Min = i
  return Min
find_min_with_for_loop([2024, 98, 131, 2, 3, 72])
print(find_min_with_for_loop([2024, 98, 131, 2, 3, 72]))

#Maximum
def find_max_with_for_loop(nums):
  Max = nums[0]
  for i in nums:
   if i > Max:
     Max = i
  return Max
find_max_with_for_loop([2024, 98, 131, 2, 3, 72])
print(find_max_with_for_loop([2024, 98, 131, 2, 3, 72]))

#6.2 While Loops
#Write two functions to manually find the minimum and maximum values in a
#list of numbers with while loops.

def find_min_with_while_loop(nums):
  Min = nums[0]
  i = 1
  while i < len(nums):
    if nums[i] < Min:
      Min = nums[i]
    i += 1
  return Min
find_min_with_while_loop([2024, 98, 131, 2, 3, 72])
print(find_min_with_while_loop([2024, 98, 131, 2, 3, 72]))

def find_max_with_while_loop(nums):
  Max = nums[0]
  i = 1
  while i < len(nums):
    if nums[i] > Max:
      Max = nums[i]
    i += 1
  return Max
find_max_with_while_loop([2024, 98, 131, 2, 3, 72])
print(find_max_with_while_loop([2024, 98, 131, 2, 3, 72]))

#7. Counting Vowels
#Write a function that takes a string as an input and returns the number of
#vowels in the string and the number of consonants in the string as tuple.
#Don’t forget about capital letters! Hint: You can use .isalpha() to check if
#a character is a letter.

def vowel_and_consonant_count(text):
  Vowels = "aeiouAEIOU"
  Number_Vowels = 0
  Number_Consonants = 0
  for characters in text:
    if characters.isalpha():
      if characters in Vowels:
        Number_Vowels += 1
      else:
        Number_Consonants += 1
  return (Number_Vowels, Number_Consonants)
vowel_and_consonant_count("UC Berkeley, founded in 1868!")
print(vowel_and_consonant_count("UC Berkeley, founded in 1868!"))

#8. Calculate Digital Root
#Write a function that takes an integer as an input and returns the sum of its
#digits.

def digital_root(num):
  String = str(num)
  ans = 0
  for i in range(len(String)):
    ans += int(String[i])
  return ans
digital_root(2468)
print(digital_root(2468))
