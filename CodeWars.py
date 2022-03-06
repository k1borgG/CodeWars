# # 1) A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base.
# x1 = int(input())
# x = x1
# sum = 0
# digit = 0
# a = x1
# while x > 0:
#     digit += 1
#     x //= 10
# while x1 > 0:
#     b = x1 % 10
#     sum += b ** digit
#     x1 //= 10
# if (sum == a):
#     print(True)
# else:
#     print(False)

# # 2) ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# def validate_pin(pin):
#     count = 0
#     for s in pin:
#         if '0' <= s <= '9':
#             count += 1
#             if count > 6:
#                 return False
#         else:
#             return False
#     if count == 4 or count == 6:
#         return True
#     else:
#         return False

# # 3) Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
# def persistence(n):
#     nStr = str(n)
#     a = []
#     countStep = 0
#     for a1 in nStr:
#         a+=a1
#     while len(a)>1:
#         countStep+=1
#         mult = 1
#         x = a
#         while len(x) > 1:
#             for c in x:
#                 mult *= int(c)
#             a = []
#             multStr = str(mult)
#             for k in multStr:
#                 a+=k
#             x = []
#     return countStep

# # 4) Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# def binary_array_to_number(arr):
#     x = 0
#     k = 0
#     for i in range(-1, -(len(arr))-1, -1):
#         x += arr[i] * (2 ** k)
#         k += 1
#     return x

# # 5) Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)
# def make_readable(seconds):
#     sec = seconds % 60
#     if (seconds // 3600) <= 99:
#         hours = seconds//3600
#         seconds = seconds%3600
#         if 1 <= hours <= 9:
#             hours = "0"+str(hours)
#         elif hours == 0:
#             hours = "00"
#         else:
#             hours = str(hours)
#     if (seconds // 60) <= 59:
#         minute = seconds // 60
#         if 1 <= minute <= 9:
#             minute = "0"+str(minute)
#         elif minute == 0:
#             minute = "00"
#         else:
#             minute = str(minute)
#         if 1 <= sec <= 9:
#             sec = "0"+str(sec)
#         elif sec==0:
#             sec = "00"
#         else:
#             sec = str(sec)
#     else:
#         minute = "00"
#     return hours+":"+minute+":"+sec

# # 6) You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer
# def find_outlier(integers):
#     countEven = 0
#     evenArr = []
#     countOdd = 0
#     oddArr = []
#     for x in integers:
#         if x % 2 == 0:
#             countEven += 1
#             evenArr.append(x)
#         else:
#             countOdd += 1
#             oddArr.append(x)
#     if countEven < countOdd:
#         return evenArr[0]
#     else:
#         return oddArr[0]

# # 7) Digital root is the recursive sum of all the digits in a number.
# def digital_root(n):
#     nStr = str(n)
#     a = []
#     for a1 in nStr:
#         a+=a1
#     while len(a)>1:
#         sum = 0
#         x = a
#         while len(x) > 1:
#             for c in x:
#                 sum += int(c)
#             a = []
#             sumStr = str(sum)
#             for k in sumStr:
#                 a+=k
#             x = []
#     return int(a[0])

# # 8) Find the missing letter
# def find_missing_letter(input):
#     alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
#     start = alphabet.index(input[0])
#     for i in range(len(input)):
#         if not input[i] == alphabet[start+i]:
#             return alphabet[start+i]

# # 9) Write a method, that gets an array of integer-numbers and return an array of the averages of each integer-number and his follower, if there is one.
# def averages(arr):
#     a = []
#     if arr != None:
#         if len(arr) <= 1:
#             return a
#         else:
#             for i in range(1,len(arr)):
#                 if ((arr[i-1]+arr[i])/2)%1==0:
#                     a.append((arr[i-1]+arr[i])//2)
#                 else:
#                     a.append((arr[i - 1] + arr[i]) / 2)
#             return a
#     else:
#         return a

# # 10) Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules.
# def score(dice):
#     finalScore = 0
#     arrCount = [0,0,0,0,0,0]
#     for i in range(0, len(dice)):
#          arrCount[dice[i]-1] += 1
#     for indexOfCount in range(0,len(arrCount)):
#         if indexOfCount == 0:
#             if arrCount[indexOfCount] == 3:
#                 finalScore += 1000
#             else:
#                 if arrCount[indexOfCount] - 3 > 0:
#                     finalScore += 1000 + (arrCount[indexOfCount] - 3) * 100
#                 else:
#                     finalScore += arrCount[indexOfCount] * 100
#         elif indexOfCount == 4:
#             if arrCount[indexOfCount] == 3:
#                 finalScore += 500
#             else:
#                 if arrCount[indexOfCount] - 3 > 0:
#                     finalScore += 500 + (arrCount[indexOfCount] - 3) * 50
#                 else:
#                     finalScore += arrCount[indexOfCount] * 50
#         else:
#             if arrCount[indexOfCount] >= 3:
#                 finalScore += 100 * (indexOfCount+1)
#     return finalScore