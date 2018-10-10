# Build Your Own Test

# This is the assert_equal function called in the assets.py file.
def assert_equal(first, second):
    message = "Expected {0} and {1} to be the same"
    message = message.format(first, second)
    assert first == second, message