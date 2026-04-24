"""
Utility module with various helper functions
"""

def fibonacci(n):
    """Generate fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list


def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def reverse_string(s):
    """Reverse a string."""
    return s[::-1]


def count_vowels(text):
    """Count vowels in a text."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)


def factorial(n):
    """Calculate factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def list_intersection(list1, list2):
    """Find common elements between two lists."""
    return list(set(list1) & set(list2))


def list_union(list1, list2):
    """Find union of two lists."""
    return list(set(list1) | set(list2))


def remove_duplicates(lst):
    """Remove duplicate elements while preserving order."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def find_max(lst):
    """Find maximum value in a list."""
    if not lst:
        return None
    return max(lst)


def find_min(lst):
    """Find minimum value in a list."""
    if not lst:
        return None
    return min(lst)


def sum_list(lst):
    """Calculate sum of all elements in a list."""
    return sum(lst)


def average(lst):
    """Calculate average of a list."""
    if not lst:
        return 0
    return sum(lst) / len(lst)


def capitalize_words(text):
    """Capitalize first letter of each word."""
    return ' '.join(word.capitalize() for word in text.split())


def is_palindrome(text):
    """Check if text is a palindrome."""
    clean = ''.join(char.lower() for char in text if char.isalnum())
    return clean == clean[::-1]


def sort_by_length(lst):
    """Sort list of strings by length."""
    return sorted(lst, key=len)


def merge_dicts(dict1, dict2):
    """Merge two dictionaries."""
    result = dict1.copy()
    result.update(dict2)
    return result


def filter_even(lst):
    """Filter even numbers from a list."""
    return [num for num in lst if num % 2 == 0]


def filter_odd(lst):
    """Filter odd numbers from a list."""
    return [num for num in lst if num % 2 != 0]


def power(base, exp):
    """Calculate base raised to power exp."""
    return base ** exp


def square(num):
    """Calculate square of a number."""
    return num ** 2


def cube(num):
    """Calculate cube of a number."""
    return num ** 3


def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def miles_to_km(miles):
    """Convert miles to kilometers."""
    return miles * 1.60934


def km_to_miles(km):
    """Convert kilometers to miles."""
    return km * 0.621371


def string_to_list(text, delimiter=' '):
    """Convert string to list using delimiter."""
    return text.split(delimiter)


def list_to_string(lst, delimiter=' '):
    """Convert list to string using delimiter."""
    return delimiter.join(str(item) for item in lst)


def is_even(num):
    """Check if number is even."""
    return num % 2 == 0


def is_odd(num):
    """Check if number is odd."""
    return num % 2 != 0


def get_file_extension(filename):
    """Get file extension from filename."""
    return filename.split('.')[-1] if '.' in filename else ''


def remove_file_extension(filename):
    """Remove file extension from filename."""
    return filename.rsplit('.', 1)[0] if '.' in filename else filename


def repeat_string(text, count):
    """Repeat string count times."""
    return text * count


def flatten_list(nested_list):
    """Flatten a nested list."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def chunk_list(lst, chunk_size):
    """Divide list into chunks of specified size."""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def rotate_list(lst, steps):
    """Rotate list by n steps."""
    if not lst:
        return lst
    steps = steps % len(lst)
    return lst[-steps:] + lst[:-steps]


def contains_duplicate(lst):
    """Check if list contains duplicates."""
    return len(lst) != len(set(lst))


def is_sorted(lst):
    """Check if list is sorted in ascending order."""
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


def unique_count(lst):
    """Count unique elements in a list."""
    return len(set(lst))


def mode_value(lst):
    """Find most common element in a list."""
    if not lst:
        return None
    return max(set(lst), key=lst.count)


if __name__ == "__main__":
    # Example usage
    print("Functions loaded successfully!")
    print(f"Fibonacci(10): {fibonacci(10)}")
    print(f"Is 17 prime?: {is_prime(17)}")
    print(f"Reverse 'hello': {reverse_string('hello')}")
    print(f"Count vowels in 'hello world': {count_vowels('hello world')}")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Average of [1,2,3,4,5]: {average([1, 2, 3, 4, 5])}")
    print(f"Is 'racecar' palindrome?: {is_palindrome('racecar')}")
