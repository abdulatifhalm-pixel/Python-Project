✅ *Python Coding Interview Questions with Answers – Part-6* 🐍💻

1️⃣ *Check if Two Lists Are Equal*  
Q: Check whether two lists contain the same elements in the same order.  
```python
def lists_equal(l1, l2):
    return l1 == l2

print(lists_equal([1, 2, 3], [1, 2, 3]))  # True  
print(lists_equal([1, 2, 3], [3, 2, 1]))  # False
```

2️⃣ *Find Intersection of Two Lists*  
Q: Return common elements without duplicates.  
```python
def intersection(l1, l2):
    return list(set(l1) & set(l2))

print(intersection([1, 2, 3, 4], [3, 4, 5]))  # [3, 4]
```

3️⃣ *Check Leap Year*  
Q: Check whether a year is a leap year.  
```python
def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

print(is_leap(2024))  # True
```

4️⃣ *Count Occurrences of an Element*  
Q: Count how many times an element appears in a list.  
```python
def count_occurrences(lst, x):
    return lst.count(x)

print(count_occurrences([1, 2, 2, 3, 2], 2))  # 3
```

5️⃣ *Check if String Contains Only Digits*  
Q: Verify whether a string has digits only.  
```python
def is_digits(s):
    return s.isdigit()

print(is_digits("12345"))  # True  
print(is_digits("123a"))   # False
```

💬 *Double Tap ❤️ for Part-7*
