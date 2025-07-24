"""
Python MNEMONIC Patterns - Organized Reference

These patterns are designed to be easy to remember and use in Python programming.
They cover common tasks and operations, providing a quick reference for developers.
Each pattern includes a brief description, example usage, and the core formula.
"""

# ============================================================================
# SECTION 1: LIST COMPREHENSIONS - BASIC PATTERNS
# ============================================================================

# [ TRANSFORM ]
# Pattern: Basic transformation of elements
s = "Hello, World!"
lowercase_chars = [char.lower() for char in s]
print(lowercase_chars)
# Formula: [transform(x) for x in collection]

# Pattern: Mathematical transformations
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared)  # [1, 4, 9, 16, 25]
# Formula: [math_operation(x) for x in collection]

# [ FILTER + TRANSFORM ]
# Pattern: Filter then transform
s = "Hello, World!"
alphanumeric_lower = [char.lower() for char in s if char.isalnum()]
print(alphanumeric_lower)
# Formula: [transform(x) for x in collection if condition(x)]

# Pattern: Extract and convert digits
s = "Hello, World122!"
digits = [int(ch) for ch in s if ch.isdigit()]
print(digits)  # [1, 2, 2]
# Formula: [convert(x) for x in collection if type_condition(x)]

# Pattern: Convert string digits to integers
s = '13243242'
converted = [int(char) for char in s]
print(converted)  # [1, 3, 2, 4, 3, 2, 4, 2]
# Formula: [int(x) for x in string]

# [ NESTED LOOPS ]
# Pattern: Flatten nested lists
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = [num for sublist in nested_list for num in sublist]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8]
# Formula: [item for sublist in nested for item in sublist]

# Pattern: Cartesian product
colors = ['red', 'green']
sizes = ['S', 'M', 'L']
combinations = [(color, size) for color in colors for size in sizes]
print(combinations)
# Formula: [(x, y) for x in collection1 for y in collection2]

# Pattern: Matrix transpose
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)
# Formula: [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# ============================================================================
# SECTION 2: DICTIONARY COMPREHENSIONS
# ============================================================================

# Pattern: Create dictionary with transformation
s = "Hello, World!"
char_mapping = {char: char.lower() for char in s if char.isalnum()}
print(char_mapping)
# Formula: {key_transform(x): value_transform(x) for x in collection if condition(x)}

# Pattern: Merge dictionaries (Python 3.5+)
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}
print(merged)  # {'a': 1, 'b': 3, 'c': 4}
# Formula: {**dict1, **dict2}

# Alternative merge method
merged_alt = dict1.copy()
merged_alt.update(dict2)
print(merged_alt)
# Formula: dict1.copy().update(dict2)

# ============================================================================
# SECTION 3: SET COMPREHENSIONS & OPERATIONS
# ============================================================================

# Pattern: Set comprehension for unique elements
s = "Hello, World!"
unique_chars = {char.lower() for char in s if char.isalnum()}
print(unique_chars)
# Formula: {transform(x) for x in collection if condition(x)}

# Pattern: Set operations
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

# Common elements (intersection)
common = set(list1) & set(list2)
common_alt = set(list1).intersection(set(list2))
print(common)  # {3, 4}
# Formula: set1 & set2 or set1.intersection(set2)

# Uncommon elements (symmetric difference)
uncommon = set(list1) ^ set(list2)
uncommon_alt = set(list1).symmetric_difference(set(list2))
print(uncommon)  # {1, 2, 5, 6}
# Formula: set1 ^ set2 or set1.symmetric_difference(set2)

# Union of sets
union = set(list1) | set(list2)
union_alt = set(list1).union(set(list2))
print(union)  # {1, 2, 3, 4, 5, 6}
# Formula: set1 | set2 or set1.union(set2)

# Difference of sets
difference = set(list1) - set(list2)
difference_alt = set(list1).difference(set(list2))
print(difference)  # {1, 2}
# Formula: set1 - set2 or set1.difference(set2)

# ============================================================================
# SECTION 4: GROUPING & AGGREGATION
# ============================================================================

# Pattern: Group items by key
from collections import defaultdict
words = ['apple', 'banana', 'apricot', 'blueberry', 'cherry']
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)
print(dict(grouped))
# Formula: defaultdict(list) + for loop with key function

# Pattern: Count occurrences
from collections import Counter
items = ['a', 'b', 'c', 'a', 'b', 'a']
counted = Counter(items)
print(counted)  # Counter({'a': 3, 'b': 2, 'c': 1})
# Formula: Counter(collection)

# Alternative counting method
counted_manual = {}
for item in items:
    counted_manual[item] = counted_manual.get(item, 0) + 1
print(counted_manual)
# Formula: dict.get(key, 0) + 1

# ============================================================================
# SECTION 5: CUMULATIVE OPERATIONS
# ============================================================================

# Pattern: Running totals
from itertools import accumulate
numbers = [1, 2, 3, 4, 5]
cumulative_sum = list(accumulate(numbers))
print(cumulative_sum)  # [1, 3, 6, 10, 15]
# Formula: list(accumulate(collection))

# Pattern: Reduce operations
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120
# Formula: reduce(operation, collection)

# ============================================================================
# SECTION 6: SEARCH & FILTER PATTERNS
# ============================================================================

# Pattern: Find maximum/minimum with conditions
numbers = [1, -2, 3, -4, 5]
max_positive = max((x for x in numbers if x > 0), default=None)
print(max_positive)  # 5
# Formula: max(generator_expression, default=value)

# Pattern: Find indices of specific elements
items = ['a', 'b', 'c', 'a', 'b', 'c']
indices = [i for i, x in enumerate(items) if x == 'a']
print(indices)  # [0, 3]
# Formula: [i for i, x in enumerate(collection) if condition(x)]

# Alternative method using filter
indices_alt = list(filter(lambda i: items[i] == 'a', range(len(items))))
print(indices_alt)
# Formula: list(filter(lambda i: collection[i] == target, range(len(collection))))

# Pattern: Find duplicates
items = ['a', 'b', 'c', 'a', 'b', 'a']
seen = set()
duplicates = set(x for x in items if x in seen or seen.add(x))
print(duplicates)  # {'a', 'b'}
# Formula: set(x for x in items if x in seen or seen.add(x))

# Alternative duplicate finding
seen_alt = {}
duplicates_alt = set()
for item in items:
    if item in seen_alt:
        duplicates_alt.add(item)
    else:
        seen_alt[item] = 1
print(duplicates_alt)

# Pattern: Get unique elements (preserving order)
items = ['a', 'b', 'c', 'a', 'b', 'a']
unique = set(items)
print(unique)  # {'a', 'b', 'c'}
# Formula: set(collection)

# Preserve order method
unique_ordered = []
for item in items:
    if item not in unique_ordered:
        unique_ordered.append(item)
print(unique_ordered)  # ['a', 'b', 'c']

# ============================================================================
# SECTION 7: SEQUENCE OPERATIONS
# ============================================================================

# Pattern: Zip and unzip lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print(zipped)  # [(1, 'a'), (2, 'b'), (3, 'c')]
# Formula: list(zip(list1, list2))

# Unzip lists
unzipped = list(zip(*zipped))
print(unzipped)  # [(1, 2, 3), ('a', 'b', 'c')]
# Alternative unzip
list1_unzipped, list2_unzipped = zip(*zipped)
print(list1_unzipped, list2_unzipped)
# Formula: zip(*zipped_list)

# Pattern: Enumerate with indices
items = ['a', 'b', 'c']
enumerated = list(enumerate(items))
print(enumerated)  # [(0, 'a'), (1, 'b'), (2, 'c')]
# Formula: list(enumerate(collection))

# Pattern: Reverse sequences
items = [1, 2, 3, 4, 5]
reversed_slice = items[::-1]
print(reversed_slice)  # [5, 4, 3, 2, 1]
# Formula: collection[::-1]

# Alternative reverse method
reversed_func = list(reversed(items))
print(reversed_func)
# Formula: list(reversed(collection))

# Pattern: Slice sequences
items = [1, 2, 3, 4, 5]
sliced = items[1:4]  # Get items from index 1 to 3
print(sliced)  # [2, 3, 4]
# Formula: collection[start:end]

# Alternative slice method
sliced_alt = items[slice(1, 4)]
print(sliced_alt)
# Formula: collection[slice(start, end)]

# ============================================================================
# SECTION 8: SORTING PATTERNS
# ============================================================================

# Pattern: Sort with custom key function
items = ['apple', 'banana', 'cherry', 'date']
sorted_by_length = sorted(items, key=len)
print(sorted_by_length)  # ['date', 'apple', 'cherry', 'banana']
# Formula: sorted(collection, key=function)

# ============================================================================
# SECTION 9: STRING MANIPULATION PATTERNS
# ============================================================================

# [ JOIN & SPLIT ]
# Pattern: Join list elements with separator
words = ['apple', 'banana', 'cherry']
sentence = ' '.join(words)
print(sentence)  # apple banana cherry
# Formula: separator.join(collection)

# Pattern: Split and clean strings
text = "apple, banana, cherry"
items = [item.strip() for item in text.split(',')]
print(items)  # ['apple', 'banana', 'cherry']
# Formula: [item.strip() for item in string.split(separator)]

# [ STRING FORMATTING ]
# Pattern: F-string with expressions
name, age = "Alice", 25
formatted = f"Hello {name}, you are {age} years old"
print(formatted)  # Hello Alice, you are 25 years old
# Formula: f"text {variable} more text"

# Pattern: Format with padding/alignment
numbers = [1, 22, 333]
padded = [f"{num:>5}" for num in numbers]  # Right-align, width 5
print(padded)  # ['    1', '   22', '  333']
# Formula: f"{value:>width}" or f"{value:<width}" or f"{value:^width}"

# ============================================================================
# SECTION 10: FILE & PATH PATTERNS
# ============================================================================

# [ PATH OPERATIONS ]
from pathlib import Path

# Pattern: Build cross-platform paths
file_path = Path("data") / "files" / "document.txt"
print(file_path)  # data/files/document.txt (or data\files\document.txt on Windows)
# Formula: Path(part1) / part2 / part3

# Pattern: Get file info
current_files = [p.name for p in Path('.').iterdir() if p.is_file()]
print(current_files)  # List of files in current directory
# Formula: [p for p in Path(directory).iterdir() if p.is_file()]

# [ FILE READING ]
# Pattern: Safe file reading with context manager (example structure)
# with open('file.txt', 'r') as f:
#     lines = [line.strip() for line in f]
# Formula: with open(file, mode) as f: [line.strip() for line in f]

# ============================================================================
# SECTION 11: ERROR HANDLING PATTERNS
# ============================================================================

# [ TRY-EXCEPT PATTERNS ]
# Pattern: Convert with fallback
def safe_convert(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

test_values = ['42', 'abc', None, '3.14']
converted = [safe_convert(val) for val in test_values]
print(converted)  # [42, 0, 0, 0]
# Formula: try: convert(value) except: return default

# Pattern: Multiple operations with single handler
operations = [lambda: 10//2, lambda: int('abc'), lambda: 42]
results = []
for op in operations:
    try:
        results.append(op())
    except:
        results.append(None)
print(results)  # [5, None, 42]
# Formula: try: operation() except: fallback_value

# ============================================================================
# SECTION 12: FUNCTIONAL PROGRAMMING PATTERNS
# ============================================================================

# [ MAP, FILTER, LAMBDA ]
# Pattern: Apply function to all elements
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]
# Formula: list(map(function, collection))

# Pattern: Filter with condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
# Formula: list(filter(condition_function, collection))

# Pattern: Chain operations with partial
from functools import partial
multiply_by_3 = partial(lambda x, y: x * y, 3)
tripled = list(map(multiply_by_3, numbers))
print(tripled)  # [3, 6, 9, 12, 15]
# Formula: partial(function, fixed_args)

# ============================================================================
# SECTION 13: DATE & TIME PATTERNS
# ============================================================================

# [ DATETIME OPERATIONS ]
from datetime import datetime, timedelta

# Pattern: Date arithmetic
today = datetime.now()
week_ago = today - timedelta(days=7)
print(f"Today: {today.strftime('%Y-%m-%d')}")
print(f"Week ago: {week_ago.strftime('%Y-%m-%d')}")
# Formula: datetime.now() ± timedelta(days=n, hours=n, minutes=n)

# Pattern: Format dates
formatted = today.strftime("%Y-%m-%d %H:%M")
print(f"Formatted: {formatted}")
# Formula: date.strftime("format_string")

# Pattern: Parse date strings
date_str = "2023-12-25"
parsed = datetime.strptime(date_str, "%Y-%m-%d")
print(f"Parsed: {parsed}")
# Formula: datetime.strptime(string, "format")

# ============================================================================
# SECTION 14: DATA VALIDATION PATTERNS
# ============================================================================

# [ VALIDATION HELPERS ]
# Pattern: Check if all/any elements meet condition
numbers = [2, 4, 6, 8]
all_even = all(x % 2 == 0 for x in numbers)
any_negative = any(x < 0 for x in numbers)
print(f"All even: {all_even}")  # True
print(f"Any negative: {any_negative}")  # False
# Formula: all(condition for item in collection)
# Formula: any(condition for item in collection)

# Pattern: Validate dictionary keys
required_keys = {'name', 'age', 'email'}
data = {'name': 'John', 'age': 30, 'email': 'john@email.com'}
is_valid = required_keys.issubset(data.keys())
print(f"Valid data: {is_valid}")  # True
# Formula: required_set.issubset(data.keys())

# ============================================================================
# SECTION 15: PERFORMANCE PATTERNS
# ============================================================================

# [ GENERATOR EXPRESSIONS ]
# Pattern: Memory-efficient processing
large_numbers = (x**2 for x in range(100) if x % 2 == 0)  # Using smaller range for demo
first_ten = [next(large_numbers) for _ in range(10)]
print(first_ten)  # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
# Formula: (expression for item in collection if condition)

# Pattern: Lazy evaluation with itertools
from itertools import islice, cycle
repeated = cycle(['A', 'B', 'C'])
first_ten_repeated = list(islice(repeated, 10))
print(first_ten_repeated)  # ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A']
# Formula: list(islice(iterator, n))

# ============================================================================
# QUICK REFERENCE FORMULAS
# ============================================================================

"""
ESSENTIAL FORMULAS SUMMARY:

List Comprehensions:
  [transform(x) for x in collection]                   # Transform
  [transform(x) for x in collection if condition(x)]   # Filter + Transform
  [item for sublist in nested for item in sublist]     # Flatten

Dictionary Comprehensions:
  {key(x): value(x) for x in collection}               # Key-Value mapping
  {**dict1, **dict2}                                   # Merge dictionaries

Set Operations:
  set1 & set2                                           # Intersection
  set1 | set2                                           # Union
  set1 - set2                                           # Difference
  set1 ^ set2                                           # Symmetric difference

Aggregation:
  Counter(collection)                                   # Count occurrences
  list(accumulate(collection))                          # Running totals
  reduce(operation, collection)                         # Reduce to single value

Search & Filter:
  max(generator, default=None)                          # Conditional max/min
  [i for i, x in enumerate(collection) if condition]    # Find indices

Sequence Operations:
  zip(list1, list2)                                     # Combine lists
  zip(*zipped_list)                                     # Unzip lists
  enumerate(collection)                                 # Add indices
  collection[::-1]                                      # Reverse
  sorted(collection, key=function)                      # Custom sort

String Manipulation:
  separator.join(collection)                            # Join elements
  [item.strip() for item in string.split(sep)]         # Split and clean
  f"text {variable} more text"                          # F-string formatting

Error Handling:
  try: operation() except: fallback_value               # Safe operations

Functional Programming:
  list(map(function, collection))                       # Apply function to all
  list(filter(condition, collection))                   # Filter elements
  partial(function, fixed_args)                         # Partial application

Date & Time:
  datetime.now() ± timedelta(days=n)                    # Date arithmetic
  date.strftime("format_string")                        # Format dates
  datetime.strptime(string, "format")                   # Parse dates

Validation:
  all(condition for item in collection)                 # Check all elements
  any(condition for item in collection)                 # Check any elements
  required_set.issubset(data.keys())                    # Validate keys

Performance:
  (expression for item in collection)                   # Generator expression
  list(islice(iterator, n))                             # Lazy evaluation
"""