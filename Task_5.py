def get_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_even_numbers(numbers))
