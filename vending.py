#Challenge

# Write a function called get_change, which accepts one argument amount (an integer). The function should return the coins needed to dispense that amount.
# The coin denominations are Euro
# (1, 2, 5, 10, 20, 50, 100, 200)
# The function should return the fewest coins possible to make the amount.
# E.g. 76c = 50, 20, 5, 1
#      44c = 20, 20, 2, 2

# First attempt (works)
# get_change = int(input("enter the amount: "))

# print(get_change)

# coin_denom = [200, 100, 50, 20, 10, 5, 2, 1]

# coins = []

# for i in coin_denom:
#     while get_change >= i:
#         new_get_change = get_change - i
#         get_change = new_get_change
#         coins.append(i)
   
# print(get_change)
# print(coins)


# Now to wrap it in a function (works)
# def get_change(x):
#     coin_denom = [200, 100, 50, 20, 10, 5, 2, 1]

#     coins = []
    
#     for i in coin_denom:
#         while x >= i:
#             y = x - i
#             x = y
#             coins.append(i)
#     return coins
    
# x = int(input("enter the amount: "))
 
# coins = get_change(x)
 
# print(coins)


# Richard's solution using Test Driven Development
# Unrefactored code;

# from byotest import assert_equal
# def get_change(amount):
    
#     coins = [200, 100, 50, 20, 10, 5, 2, 1]
    
#     if amount == 0:
#         return []
    
#     if amount in coins:
#         return [amount]
    
#     change = []
#     for c in coins:
#         while c <= amount:
#             change.append(c)
#             amount = amount - c
#     return change
    
# assert_equal(get_change(0), [])
# assert_equal(get_change(1), [1])
# assert_equal(get_change(2), [2])
# assert_equal(get_change(5), [5])
# assert_equal(get_change(10), [10])
# assert_equal(get_change(20), [20])
# assert_equal(get_change(50), [50])
# assert_equal(get_change(100), [100])
# assert_equal(get_change(200), [200])
# assert_equal(get_change(3), [2, 1])
# assert_equal(get_change(8), [5, 2, 1])
# assert_equal(get_change(76), [50, 20, 5, 1])
# assert_equal(get_change(4), [2, 2])

# print("All tests pass")


# Refactored code;

# from byotest import assert_equal

# def get_change(amount):
    
#     coins = [200, 100, 50, 20, 10, 5, 2, 1]
    
#     change = []

#     for c in coins:
#         while c <= amount:
#             change.append(c)
#             amount = amount - c

#     return change



# assert_equal(get_change(0), [])

# assert_equal(get_change(1), [1])
# assert_equal(get_change(2), [2])
# assert_equal(get_change(5), [5])
# assert_equal(get_change(10), [10])
# assert_equal(get_change(20), [20])
# assert_equal(get_change(50), [50])
# assert_equal(get_change(100), [100])
# assert_equal(get_change(200), [200])


# assert_equal(get_change(3), [2, 1])
# assert_equal(get_change(8), [5, 2, 1])
# assert_equal(get_change(76), [50, 20, 5, 1])


# assert_equal(get_change(4), [2, 2])

# print("All tests pass")


# With multiple denominations

from byotest import assert_equal

euro_coins = [200, 100, 50, 20, 10, 5, 2, 1]
us_coins = [100, 50, 25, 10, 5, 1]
skorea_coins = [500, 100, 50, 10, 5]

def get_change(amount, coins = euro_coins):
    
    change = []

    for c in coins:
        while c <= amount:
            change.append(c)
            amount = amount - c

    return change


assert_equal(get_change(0), [])

assert_equal(get_change(1), [1])
assert_equal(get_change(2), [2])
assert_equal(get_change(5), [5])
assert_equal(get_change(10), [10])
assert_equal(get_change(20), [20])
assert_equal(get_change(50), [50])
assert_equal(get_change(100), [100])
assert_equal(get_change(200), [200])

assert_equal(get_change(3), [2, 1])
assert_equal(get_change(8), [5, 2, 1])
assert_equal(get_change(76), [50, 20, 5, 1])

assert_equal(get_change(4), [2, 2])


assert_equal(get_change(76, us_coins), [50, 25, 1])

assert_equal(get_change(575, skorea_coins), [500, 50, 10, 10, 5])

print("All tests pass")