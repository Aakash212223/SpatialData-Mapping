# 📝 Worksheet: 02 - Working with Data

Use this worksheet to review and reinforce your understanding of Python data containers.

---

## 🧠 Section 1: Lists

1. What method adds an item to the end of a list?  
   `Answer:` _append()___________________________

2. How can you remove an item from a list by value?  
   `Answer:` _remove()___________________________

3. What’s the result of this code?

```python
nums = [2, 4, 6]
nums.append(8)
print(nums)
```

   `Answer:` __[2, 4, 6, 8]__________________________

---

### ✏️ Task: List Practice

```python
# Create a list of your top 3 favorite foods.
# Add another food to the list.
# Remove one item and print the list.
```
foods = ["Pizza", "Burger", "Pasta"]

foods.append("Pasta")

foods.remove("Burger")

print(foods)
---

## 🔒 Section 2: Tuples

4. What is a key difference between a list and a tuple?  
   `Answer:` _Lists are mutable (can be changed), while tuples are immutable (cannot be changed).___________________________

5. Can you change the contents of a tuple once it is created? Why or why not?  
   `Answer:` No. Tuples are immutable, so their contents cannot be modified after creation.____________________________

---

### ✏️ Task: Tuple Practice

```python
# Create a tuple with your favorite 3 numbers.
# Unpack it into three variables and print each.
```
numbers = (1, 5, 10)

a, b, c = numbers

print(a)
print(b)
print(c)
---

## 🔑 Section 3: Dictionaries

6. What does the `.get()` method do differently from accessing a key directly?  
   `Answer:` .get() returns a default value (or None) if the key does not exist, instead of raising an error.____________________________

7. How do you loop through both keys and values in a dictionary?  
   `Answer:` Using the items() method.____________________________

---

### ✏️ Task: Dictionary Practice

```python
# Create a dictionary with keys: 'name', 'age', and 'hobby'.
# Print each key and value in the format "key: value".
```
person = {
    "name": "Aakash",
    "age": 24,
    "hobby": "Trading"
}

for key, value in person.items():
    print(f"{key}: {value}")
---

## 🧾 Submit Checklist

- [✔] I practiced creating and modifying lists.
- [✔] I understand how tuples are different from lists.
- [✔] I accessed and looped through dictionary items.
