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

