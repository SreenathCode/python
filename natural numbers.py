def find_natural_numbers(limit):
    natural_numbers = []
    for i in range(1, limit + 1):
        natural_numbers.append(i)
    return natural_numbers

# Example usage:
limit = 10
result = find_natural_numbers(limit)
print(result)
