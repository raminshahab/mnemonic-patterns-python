'''
Python MNEMONIC Patterns

These patterns are designed to be easy to remember and use in Python programming.
They cover common tasks and operations, providing a quick reference for developers.
Each pattern includes a brief description and an example of its usage.


'''

# [ Loop, Transform ]
# Pattern: Basic transformation
s = "Hello, World!"
[char.lower() for char in s]
# Formula [transform(x) for x in collection]

# Pattern: Square numbers in a list
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(squared)
# Formula [transform(x) for x in collection]


# [ Loop, Filter, Transform ]
# Pattern: Filter transformation
s = "Hello, World!"
[char.lower() for char in s if char.isalnum()]
# Formula [transform(x) for x in collection if condition(x)]

# Pattern: Get digits from a string
s = "Hello, World122!"
[int(ch) for ch in s if ch.isdigit()]
# Formula [int(x) for x in s if x.isdigit()]

# Convert list of strings to integers without fitering into a new list -> [1, 3, 2, 4, 3, 2, 4, 2] 
s = '13243242'
converted = [int(strs) for strs in s]
print(converted)

# Flatten nested list 
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = [num for sublist in nested_list for num in sublist]
print(flattened)

s = 1223234 #You can't do this because s is an integer and not iterable 
# converted = [str(nums) for nums in s]
print(converted)

# Pattern: Cartesian product
colors = ['red', 'green']
sizes = ['S', 'M', 'L']
cp = [(color, size) for color in colors for size in sizes]
print(cp)
# Formula [(x, y) for x in collection1 for y in collection2]

# Pattern: Transpose a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)

# Patterns using data structures
# [ Loop, Transform, Data Structure ]
# Pattern: Dictionary comprehension
s = "Hello, World!"
{char: char.lower() for char in s if char.isalnum()}
# Formula {key_transform(x): value_transform(x) for x in collection if condition(x)}

# Pattern: Set comprehension
s = "Hello, World!"
{char.lower() for char in s if char.isalnum()}
# Formula {transform(x) for x in collection if condition(x)}

# Pattern: Grouping items
from collections import defaultdict
words = ['apple', 'banana', 'apricot', 'blueberry', 'cherry']
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)
print(dict(grouped))
# Formula {key_transform(x): [x for x in collection if key_condition(x)]}

# Pattern: Running totals/cumulative operations
from itertools import accumulate
numbers = [1, 2, 3, 4, 5]
cumulative_sum = list(accumulate(numbers))
print(cumulative_sum)

# Multiply all elements in a list
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# Pattern: Finding maximum/minimum with conditions
numbers = [1, -2, 3, -4, 5]
max_positive = max((x for x in numbers if x > 0), default=None)
print(max_positive)

# Pattern: Finding common elements in lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)
print(common)

# alternative way
print(set(list1).intersection(set(list2)))

# Pattern: Finding uncommon elements in lists
common = set(list1) ^ set(list2)
print(common)

# alternate way
print(set(list1).symmetric_difference(set(list2)))

# Union of two lists
union = set(list1) | set(list2)
print(union)

# alternate way
print(set(list1).union(set(list2)))

# Difference of two lists
difference = set(list1) - set(list2)
print(difference)  # Elements in list1 not in list2

# alternate way
print(set(list1).difference(set(list2)))

# Pattern: Merging dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}
print(merged)

# alternate way
merged = dict1.copy()
merged.update(dict2)
print(merged)

# Pattern: Zipping lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print(zipped)

# Unzipping lists
unzipped = list(zip(*zipped))
print(unzipped)
# alternate way
list1_unzipped, list2_unzipped = zip(*zipped)
print(list1_unzipped, list2_unzipped)

# Pattern: Enumerating items
items = ['a', 'b', 'c']
enumerated = list(enumerate(items))
print(enumerated)

# Pattern: Reversing a list
items = [1, 2, 3, 4, 5]
reversed_items = items[::-1]
print(reversed_items)
# alternate way
reversed_items = list(reversed(items))
print(reversed_items)

# Pattern: Slicing a list
items = [1, 2, 3, 4, 5]
sliced = items[1:4]  # Get items from index 1 to 3
print(sliced)
# alternate way
sliced = items[slice(1, 4)]
print(sliced)

# Pattern: Finding indices of elements
items = ['a', 'b', 'c', 'a', 'b', 'c']
indices = [i for i, x in enumerate(items) if x == 'a']
print(indices)

# alternate way
indices = list(filter(lambda i: items[i] == 'a', range(len(items))))
print(indices)

# Pattern: Counting occurrences
from collections import Counter
items = ['a', 'b', 'c', 'a', 'b', 'a']
counted = Counter(items)
print(counted)
# alternate way
counted = {}
for item in items:
    counted[item] = counted.get(item, 0) + 1
print(counted)

# Pattern: Finding duplicates
items = ['a', 'b', 'c', 'a', 'b', 'a']
seen = set()
duplicates = set(x for x in items if x in seen or seen.add(x))
print(duplicates)

# alternate way
seen = {}
duplicates = set()
for item in items:
    if item in seen:
        duplicates.add(item)
    else:
        seen[item] = 1
print(duplicates)

# Pattern: Finding unique elements
items = ['a', 'b', 'c', 'a', 'b', 'a']
unique = set(items)
print(unique)

# alternate way
unique = []
for item in items:
    if item not in unique:
        unique.append(item)
print(unique)

# Pattern: Sorting with custom keys
items = ['apple', 'banana', 'cherry', 'date']
sorted_items = sorted(items, key=len)
print(sorted_items)


 