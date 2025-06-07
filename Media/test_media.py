from media import media

# Test with integers
numbers = [1, 2, 3, 4, 5]
print(f"Average of {numbers} is: {media(numbers)}")

# Test with floating point numbers
float_numbers = [1.5, 2.5, 3.5]
print(f"Average of {float_numbers} is: {media(float_numbers)}")

# Test with empty list
empty = []
print(f"Average of empty list is: {media(empty)}")
