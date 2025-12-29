✅ *Python Coding Interview Questions with Answers. Part-5* 🐍💻

1️⃣ Find Missing Number in a List  
Q: Find the missing number from 1 to n.  
```python
def find_missing(nums, n):  
    return n * (n + 1) // 2 - sum(nums)

print(find_missing([1, 2, 4, 5], 5))  # Output: 3
```

2️⃣ Swap Two Variables Without Temp  
Q: Swap two numbers without using a third variable.  
```python
a, b = 5, 10  
a, b = b, a  
print(a, b)  # Output: 10 5
```

3️⃣ Count Character Frequency  
Q: Count frequency of each character in a string.  
```python
from collections import Counter

def char_frequency(s):  
    return Counter(s)

print(char_frequency("python"))
```

4️⃣ Check Armstrong Number  
Q: Check if a number is an Armstrong number.  
```python
def is_armstrong(n):  
    digits = [int(d) for d in str(n)]  
    return n == sum(d**len(digits) for d in digits)

print(is_armstrong(153))  # Output: True
```

5️⃣ Reverse Words in a Sentence  
Q: Reverse words while keeping order.  
```python
def reverse_words(s):  
    return " ".join(word[::-1] for word in s.split())

print(reverse_words("Python is fun"))  
Output: nohtyP si nuf
```

💬 *Double Tap ❤️ for Part-6*
