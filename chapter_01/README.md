# Chapter 1: Python Primer

This chapter covers fundamental Python programming concepts including:
- Basic Python syntax and data types
- Control flow structures
- Functions and parameter passing
- Python's built-in classes and operations
- List comprehensions and generators
- Exception handling

## Exercises Completed

### Reinforcement Exercises (R-1.1 to R-1.12)
Basic exercises covering:
- Simple functions (multiples, even numbers)
- Sequence operations (min/max without built-ins)
- Sum operations and comprehensions
- Python indexing and range operations
- Random module implementations

### Creativity Exercises (C-1.13 to C-1.28)
More challenging problems including:
- List reversal and manipulation
- String processing (vowel counting, punctuation removal)
- Generator functions
- Vector operations (p-norm calculations)
- Understanding Python's mutability model

### Project Exercises (P-1.29 to P-1.36)
Comprehensive projects:
- Permutation generation
- Calculator simulations
- Change-making algorithms
- Birthday paradox simulation
- Word frequency counting

## Key Learnings

1. **Immutability vs Mutability**: Understanding how Python handles immutable types (int, str) vs mutable types (list, dict)
2. **List Comprehensions**: Powerful syntax for creating lists based on existing sequences
3. **Generator Functions**: Memory-efficient iteration using `yield`
4. **Exception Handling**: Proper use of try-except blocks for error management
5. **Algorithm Efficiency**: Early introduction to considering performance (e.g., factor generation)

## Notable Implementations

### Efficient Factor Generation (C-1.27)
```python
def generate_factors_in_order(n):
    """Generate factors in increasing order efficiently."""
    # Only iterate up to sqrt(n)
    # Yield factors in sorted order
```

### P-Norm Vector Function (C-1.28)
```python
def norm(v, p=2):
    """Calculate the p-norm of a vector, defaulting to Euclidean norm."""
    # Demonstrates default parameters and mathematical operations
```

### Birthday Paradox Simulation (P-1.35)
```python
def test_birthday_paradox():
    """Empirically test the birthday paradox with simulations."""
    # Demonstrates probability and random number generation
```

## Running the Solutions

### Import and Use
```python
from solutions import is_multiple, minmax, norm, count_vowels

# Test individual functions
print(is_multiple(15, 3))  # True
print(minmax([3, 1, 4, 1, 5, 9, 2, 6]))  # (1, 9)
print(norm([3, 4]))  # 5.0 (Euclidean norm)
print(count_vowels("Hello World"))  # 3
```

### Run Tests
```bash
cd tests
python test_runner.py
```

## Alternative Implementations

Many exercises include alternative implementations to demonstrate different approaches:
- `is_even()` vs `is_even_alternative()` - Loop-based vs bitwise operations
- `all_distinct()` vs `all_distinct_alternative()` - Manual tracking vs set comparison
- `dot_product()` vs `dot_product_alternative()` - Loop vs list comprehension

## Notes

- All functions include comprehensive docstrings
- Edge cases are handled with assertions where appropriate
- Code prioritizes readability and educational value
- Some solutions demonstrate both explicit and Pythonic approaches

## Next Steps

Chapter 2 will build on these foundations to explore object-oriented programming in Python, including:
- Class definitions and inheritance
- Encapsulation and information hiding
- Operator overloading
- Design patterns
