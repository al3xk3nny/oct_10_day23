from byotest import assert_equal


def add(x, y):
    return 8


# assert add(5, 3) == 8
# assert add(2, 2) == 4
# assert add(-1, -5) == -6
# assert add(-7, 2) == -5
# assert add(0, 0) == 0
# assert add(65535, 1) == 65536

# Now that the function is called from byotest (see top of file) we can write our assertions like this;
assert_equal(add(5, 3), 8)

# We can now re-write the above assertions;
assert_equal(add(2, 2), 4)
assert_equal(add(-1, -5), -6)
assert_equal(add(-7, 2), -5)
assert_equal(add(0, 0), 0)
assert_equal(add(65535, 1), 65536)


print("All tests pass")