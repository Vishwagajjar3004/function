import re

def clean_text(text):
    """
    Clean a string by:
    - Converting to lowercase
    - Removing extra spaces
    - Removing special characters
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return " ".join(text.split())

def safe_divide(a, b):
    """
    Safely divide two numbers.
    Returns None if division by zero occurs.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None

def flatten_dict(d, parent_key="", sep="."):
    """
    Flatten a nested dictionary into a single-level dictionary.
    Example:
    {'a': {'b': 1}} -> {'a.b': 1}
    """
    items = {}

    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key

        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key, sep))
        else:
            items[new_key] = value

    return items

def chunk_list(lst, size):
    """
    Split a list into smaller chunks of given size.
    """
    return [lst[i:i + size] for i in range(0, len(lst), size)]

def count_words(text):
    """
    Count the number of words in a string.
    """
    return len(text.split())

print("=" * 50)
print("TESTING clean_text()")
print("=" * 50)

print(clean_text("Hello World!"))
print(clean_text("Python   Programming"))
print(clean_text("Welcome@2025!!!"))

print("\n" + "=" * 50)
print("TESTING safe_divide()")
print("=" * 50)

print(safe_divide(10, 2))
print(safe_divide(5, 0))
print(safe_divide(100, 4))

print("\n" + "=" * 50)
print("TESTING flatten_dict()")
print("=" * 50)

print(flatten_dict({"a": {"b": 1}}))

print(flatten_dict({
    "user": {
        "name": "john",
        "age": 20
    }
}))

print(flatten_dict({
        "address": {
            "city": "Bhavnagar"
        }
}))

print("\n" + "=" * 50)
print("TESTING chunk_list()")
print("=" * 50)

print(chunk_list([1, 2, 3, 4, 5], 2))
print(chunk_list([10, 20, 30, 40], 3))
print(chunk_list(["a", "b", "c", "d"], 2))

print("\n" + "=" * 50)
print("TESTING count_words()")
print("=" * 50)

print(count_words("Hello World"))
print(count_words("Python is awesome"))
print(count_words("I am learning Python functions"))