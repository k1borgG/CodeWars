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


def validate_pin(pin):
    count = 0
    for s in pin:
        if '0' <= s <= '9':
            count += 1
            if count > 6:
                return False
        else:
            return False
    if count == 4 or count == 6:
        return True
    else:
        return False