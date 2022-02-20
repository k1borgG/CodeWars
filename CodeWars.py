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