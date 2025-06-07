from media import (
    media,          # Original Spanish name kept
    median,         # New English name
    mode,          # New English name
    variance,      # New English name
    standard_deviation  # New English name
)

# Test data
numbers = [2, 4, 4, 4, 5, 5, 7, 9]

print("Testing media-calc v0.2.4:")
print("-" * 30)
print(f"Data: {numbers}")
print(f"Mean (media): {media(numbers)}")
print(f"Median: {median(numbers)}")
print(f"Mode: {mode(numbers)}")
print(f"Variance: {variance(numbers)}")
print(f"Standard Deviation: {standard_deviation(numbers)}")
