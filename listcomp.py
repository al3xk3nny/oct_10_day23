from byotest import assert_equal

# This function counts the number of uppercase letters in a string.
# def foo(text):
#     count = 0
#     for c in text:
#         if c.isupper():
#             count += 1
#     return count
    
# List comprehension
def foo(text):
     return len([c for c in text if c.isupper()])
     
# print(foo("Hello"))     
    

assert_equal(foo(""), 0)
assert_equal(foo("Hello"), 1)
assert_equal(foo("HeLlo"), 2)

print("All tests pass")