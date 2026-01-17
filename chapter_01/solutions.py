# ========== Reinforcement Exercises ==========


"""
R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
"""

def is_multiple(n, m):

    """
    Return True if n is a multiple of m, False otherwise.
    """
    
    if m == 0:
        return False  # Avoid division by zero
    return n % m == 0


# --------------------------------------------------------------------------------------------

"""
R-1.2 Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""

def is_even(k):

    """
    Return True if k is even, False otherwise.
    """
    
    if not k < 0:
       
        while k >= 2:
            k -= 2
    
    else:
        while k <= -2:
            k += 2
    return k == 0

def is_even_alternative(k):

    """
    Alternative implementation to return True if k is even, False otherwise.
    """
    
    return (k & 1) == 0  # Using bitwise AND to check evenness


# --------------------------------------------------------------------------------------------

"""
R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""

def minmax(data):

    """
    Return a tuple containing the smallest and largest numbers in the data sequence.
    """
    
    assert len(data) > 0, "The input sequence must contain at least one number."
    
    minimum = data[0]
    maximum = data[0]
    
    for number in data:
        if number < minimum:
            minimum = number
        elif number > maximum:
            maximum = number
    
    return (minimum, maximum)

# --------------------------------------------------------------------------------------------

"""
R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""

def sum_of_squares(n):

    """
    Return the sum of the squares of all positive integers smaller than n.
    """
    
    assert n > 0, "Input must be a positive integer."
    
    total = 0
    for i in range(1, n):
        total += i * i
    
    return total

# --------------------------------------------------------------------------------------------

"""
R-1.5 Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python’s comprehension syntax and the built-in sum function.
"""

def sum_of_squares_inbuilt(n):

    """
    Return the sum of the squares of all positive integers smaller than n using built-in functions.
    """
    
    assert n > 0, "Input must be a positive integer."
    
    return sum(i * i for i in range(1, n))

# --------------------------------------------------------------------------------------------

"""
R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""

def sum_of_squares_odd(n):

    """
    Return the sum of the squares of all odd positive integers smaller than n.
    """
    
    assert n > 0, "Input must be a positive integer."
    
    total = 0
    for i in range(1, n, 2):  # Start from 1 and step by 2 to get odd numbers
        total += i * i
    
    return total

# --------------------------------------------------------------------------------------------

"""
R-1.7 Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function.
"""

def sum_of_squares_odd_inbuilt(n):

    """
    Return the sum of the squares of all odd positive integers smaller than n using built-in functions.
    """
    
    assert n > 0, "Input must be a positive integer."
    
    return sum(i * i for i in range(1, n) if i % 2 != 0)

# --------------------------------------------------------------------------------------------

"""
R-1.8 Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for in-
dex−n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?
"""

def negative_index_equivalent(s, k):

    """
    Return the equivalent non-negative index for a negative index k in string s.
    """
    
    n = len(s)
    assert -n <= k < 0, "Index k must be in the range -n <= k < 0."
    
    j = n + k
    return j

# --------------------------------------------------------------------------------------------

"""
R-1.9 What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
"""

def generate_range():

    """
    Return a range object that produces values 50, 60, 70, 80.
    """
    
    return range(50, 90, 10)  # Start at 50, end before 90, step by 10

# --------------------------------------------------------------------------------------------

"""
R-1.9 What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?
"""

def generate_range():

    """
    Return a range object that produces values 50, 60, 70, 80.
    Anything greater than 80 and less than or equal to 90 would 
    also work as the stop parameter, as long as the step parameter 
    is set to 10.

    Using 90 as the stop parameter here.
    """
    
    return range(50, 90, 10)  # Start at 50, end before 90, step by 10

# --------------------------------------------------------------------------------------------

"""
R-1.10 What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0,−2,−4,−6,−8?
"""

def generate_reverse_range():

    """
    Return a range object that produces values 8, 6, 4, 2, 0, -2, -4, -6, -8.
    """
    
    return range(8, -10, -2)  # Start at 8, end before -10, step by -2

# --------------------------------------------------------------------------------------------

"""
R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""

def generate_powers_of_two():

    """
    Return a list containing the powers of two from 2^0 to 2^8.
    """
    
    return [2**k for k in range(9)]  # List comprehension for powers of two

# --------------------------------------------------------------------------------------------

"""
R-1.12 Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module in-
cludes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function.
"""

def random_choice(data):

    """
    Return a random element from the non-empty sequence data using randrange.
    """
    import random
    assert len(data) > 0, "The input sequence must be non-empty."
    
    index = random.randrange(0, len(data))  # Get a random index in the range of data
    return data[index]  # Return the element at the random index

# --------------------------------------------------------------------------------------------

# ========== Creativity Exercises ==========

"""
C-1.13 Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""

def reverse_list(data):

    """
    Return a new list that is the reverse of the input list data.
    """
    
    n = len(data)
    reversed_data = [0] * n  # Create a new list of the same length
    
    for i in range(n):
        reversed_data[i] = data[n - 1 - i]  # Assign elements in reverse order
    
    return reversed_data

# --------------------------------------------------------------------------------------------

"""
C-1.14 Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""

def has_odd_product_pair(data):

    """
    Return True if there is a distinct pair of numbers in data whose product is odd, False otherwise.
    """

    assert len(data) >= 2, "The input sequence must contain at least two numbers."
    
    odd_numbers = [num for num in data if num % 2 != 0]  # Extract odd numbers from the data (Since product of two odd numbers is odd)
    
    return len(odd_numbers) >= 2  # At least two odd numbers are needed for an odd product pair

# --------------------------------------------------------------------------------------------

"""
C-1.15 Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""

def all_distinct(data):

    """
    Return True if all numbers in data are distinct, False otherwise.
    """
    
    seen = set()  # Create an empty set to track seen numbers
    
    for number in data:
        if number in seen:
            return False  # Duplicate found
        seen.add(number)  # Add number to the set
    
    return True  # All numbers are distinct


def all_distinct_alternative(data):
    
    """
    Alternative implementation to return True if all numbers in data are distinct, False otherwise.
    """
    
    return len(data) == len(set(data))  # Compare length of data with length of set of data

# --------------------------------------------------------------------------------------------

"""
C-1.16 In our implementation of the scale function (page 25), the body of the loop
executes the command data[j] = factor. We have discussed that numeric
types are immutable, and that use of the= operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?
"""

# Answer: In Python, when we use the statement data[j] = factor inside the scale function, 
# we are not modifying the integer object itself (which is immutable), but rather, we are modifying 
# the list object that contains the integer. The list is mutable, so we can change its elements.
#  The assignment creates a new integer object for the element at index j and updates the list to 
# reference this new object. This change to the list is reflected outside the function because the 
# list object itself is modified, not the integer objects it contains.

# --------------------------------------------------------------------------------------------

"""
C-1.17 Had we implemented the scale function (page 25) as follows, does it work
properly?
def scale(data, factor):
    for val in data:
        val = factor
Explain why or why not.
"""

# Answer: No, this implementation of the scale function does not work properly. 
# In this version, the loop iterates over each element in the data list,
# but the variable val is just a local reference to each element.
# When we assign val = factor, we are only changing the local reference val to point to
# a new integer object (factor), and this does not affect the original list data.
# As a result, the elements in the data list remain unchanged after the function call.

# --------------------------------------------------------------------------------------------

"""
C-1.18 Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
"""

def generate_custom_list():

    """
    Return a list containing the values [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
    """
    
    return [k * (k + 1) for k in range(10)]  # List comprehension for the desired values

# --------------------------------------------------------------------------------------------

"""
C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
"""

def generate_alphabet_list():

    """
    Return a list containing the lowercase letters of the English alphabet.
    """
    
    return [chr(ord('a') + k) for k in range(26)]  # List comprehension for letters a to z

# --------------------------------------------------------------------------------------------

"""
C-1.20 Python’s random module includes a function shuﬄe(data) that accepts a
list of elements and randomly reorders the elements so that each possi-
ble order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuﬄe function.
"""

def shuffle(data):

    """
    Shuffle the list data in place using only the randint function.
    """
    import random
    n = len(data)
    
    for i in range(n):
        j = random.randint(0, n - 1)  # Get a random index between 0 and n-1
        print (i, j)
        data[i], data[j] = data[j], data[i]  # Swap elements at indices i and j
    return data

# --------------------------------------------------------------------------------------------

"""
C-1.21 Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
"""

def reverse_input_lines():

    """
    Read lines from standard input until EOFError is raised, then output them in reverse order.
    """
    
    lines = []
    
    print("Enter lines of text (type Ctrl-D to end input):")
    
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        print("\nEnd of input reached.")
        pass  # End of input reached
    
    print("\nLines in reverse order:")
    for line in lines[::-1]:
        print(line)

# --------------------------------------------------------------------------------------------

"""
C-1.22 Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i]· b[i], for i= 0,...,n− 1.
"""

def dot_product(a, b):

    """
    Return the dot product of two arrays a and b of the same length.
    """
    
    assert len(a) == len(b), "Input arrays must have the same length."
    
    n = len(a)
    c = [0] * n  # Create an array of length n to store the result
    
    for i in range(n):
        c[i] = a[i] * b[i]  # Compute the product of corresponding elements
    
    return c

def dot_product_alternative(a, b):
    
    """
    Alternative implementation to return the dot product of two arrays a and b of the same length.
    """
    
    assert len(a) == len(b), "Input arrays must have the same length."
    
    return [a[i] * b[i] for i in range(len(a))]  # List comprehension for the dot product

# --------------------------------------------------------------------------------------------

"""
C-1.23 Give an example of a Python code fragment that attempts to write an ele-
ment to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don’t try buffer overflow attacks in Python!”
"""

def write_to_list_with_exception_handling(data, index, value):

    """
    Attempt to write value to data at the specified index, handling out-of-bounds exceptions.
    """
    
    try:
        data[index] = value  # Attempt to write to the list at the given index
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")  # Handle out-of-bounds exception


def write_to_list_with_exception_handling_alternative(data, index, value):
    """
    Alternative implementation to attempt to write value to data at the specified index, handling out-of-bounds exceptions.
    """
    
    if index < 0 or index >= len(data):
        print("Don't try buffer overflow attacks in Python!")  # Handle out-of-bounds condition
        print ("Tried to access index:", index, "but valid indices are from 0 to", len(data)-1, ". Retry by giving a valid index.")
        index = int(input("Enter a valid index: "))
        write_to_list_with_exception_handling_alternative(data, index, value)  # Retry
    else:
        data[index] = value  # Write to the list at the given index


# --------------------------------------------------------------------------------------------

"""
C-1.24 Write a short Python function that counts the number of vowels in a given
character string.
"""

def count_vowels(s):

    """
    Return the number of vowels in the given string s.
    """
    
    vowels = 'aeiou'  # Define vowels
    count = 0
    
    for char in str(s).lower():  # Convert string to lowercase for uniformity
        if char in vowels:
            count += 1  # Increment count for each vowel found
    
    return count

# --------------------------------------------------------------------------------------------

"""
C-1.25 Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For exam-
ple, if given the string "Let s try, Mike.", this function would return
"Lets try Mike"
"""

def remove_punctuation(s):

    """
    Return a copy of the string s with all punctuation removed.
    """
    import string
    
    return ''.join(char for char in s if char not in string.punctuation)  # Use string.punctuation to filter out punctuation characters

def remove_punctuation_alternative(s):
    
    """
    Alternative implementation to return a copy of the string s with all punctuation removed.
    """
    punctuation_set = set('!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')  # Define a set of punctuation characters
    
    return ''.join(char for char in s if char not in punctuation_set)  # Filter out punctuation characters

# --------------------------------------------------------------------------------------------

"""
C-1.26 Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a + b= c,” “a = b− c,” or “a ∗ b= c.”
"""

def check_arithmetic_formulas(a, b, c):

    """
    Check if the integers a, b, and c can be used in a correct arithmetic formula.
    """
    
    if a + b == c:
        return f"{a} + {b} = {c}"
    elif a - b == c:
        return f"{a} - {b} = {c}"
    elif a * b == c:
        return f"{a} * {b} = {c}"
    elif b != 0 and a / b == c:
        return f"{a} / {b} = {c}"
    elif a == b + c:
        return f"{a} = {b} + {c}"
    elif a == b - c:
        return f"{a} = {b} - {c}"
    elif a == b * c:
        return f"{a} = {b} * {c}"
    elif c != 0 and a == b / c:
        return f"{a} = {b} / {c}"
    else:
        return "No valid arithmetic formula found."
    

def check_arithmetic_formulas_alternative(a, b, c):

    """
    Alternative implementation to check if the integers a, b, and c can be used in a correct arithmetic formula.
    """
    
    formulas = [
        (a + b == c, f"{a} + {b} = {c}"),
        (a - b == c, f"{a} - {b} = {c}"),
        (a * b == c, f"{a} * {b} = {c}"),
        (b != 0 and a / b == c, f"{a} / {b} = {c}"),
        (a == b + c, f"{a} = {b} + {c}"),
        (a == b - c, f"{a} = {b} - {c}"),
        (a == b * c, f"{a} = {b} * {c}"),
        (c != 0 and a == b / c, f"{a} = {b} / {c}")
    ]
    
    for condition, formula in formulas:
        if condition:
            return formula  
    
    return "No valid arithmetic formula found."     

# --------------------------------------------------------------------------------------------

"""
C-1.27 In Section 1.8, we provided three different implementations of a generator
that computes factors of a given integer. The third of those implementa-
tions, from page 41, was the most efficient, but we noted that it did not
yield the factors in increasing order. Modify the generator so that it reports
factors in increasing order, while maintaining its general performance ad-
vantages.
"""

def generate_factors_in_order(n):

    """
    Generate factors of the given integer n in increasing order.
    """
    
    small_factors = []
    large_factors = []
    
    k = 1
    while k * k <= n:
        if n % k == 0:
            small_factors.append(k)  # Store small factor
            if k != n // k:
                large_factors.append(n // k)  # Store corresponding large factor
        k += 1
    
    # Combine small factors and reversed large factors to get all factors in order
    for factor in small_factors:
        yield factor
    for factor in reversed(large_factors):
        yield factor


# --------------------------------------------------------------------------------------------

"""
C-1.28 The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is de-
fined as
∥v∥=
p
vp
1 + vp
2 +· · · + vp
n.
For the special case of p= 2, this results in the traditional Euclidean
norm, which represents the length of the vector. For example, the Eu-
clidean norm of a two-dimensional vector with coordinates (4,3) has a
Euclidean norm of √42 + 32 = √16 + 9= √25= 5. Give an implemen-
tation of a function named norm such that norm(v, p) returns the p-norm
value of v and norm(v) returns the Euclidean norm of v. You may assume
that v is a list of numbers.
"""

def norm(v, p=2):

    """
    Return the p-norm of the vector v. Default is Euclidean norm (p=2).
    """
    assert p > 0, "Parameter p must be a positive number."
    assert len(v) > 0, "Vector v must contain at least one component."
    assert all(isinstance(component, (int, float)) for component in v), "All components of vector v must be numbers."
    
    total = sum(abs(component) ** p for component in v)  # Sum of absolute values raised to power p
    return total ** (1 / p)  # Take the p-th root of the total

# --------------------------------------------------------------------------------------------

# ========== Projects ==========

"""
P-1.29 Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
"""

def generate_permutations(characters):

    """
    Generate all possible strings formed by using the characters exactly once.
    """
    from itertools import permutations
    
    return [''.join(p) for p in permutations(characters)]  # Generate permutations and join to form strings


def generate_permutations_alternative(characters):
    
    """
    Alternative implementation to generate all possible strings formed by using the characters exactly once.
    """
    def backtrack(path, remaining, result):
        if not remaining:
            result.append(''.join(path))  # Add the current permutation to the result
            return
        for i in range(len(remaining)):
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:], result)  # Recurse with updated path and remaining characters
    
    result = []
    backtrack([], list(characters), result)
    return result

# --------------------------------------------------------------------------------------------

"""
P-1.30 Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
"""

def count_divisions_by_two(n):

    """
    Return the number of times n must be divided by 2 before getting a value less than 2.
    """
    
    assert n > 2, "Input must be a positive integer greater than 2."
    
    count = 0
    while n >= 2:
        n /= 2  # Divide n by 2
        count += 1  # Increment the count
    
    return count

# --------------------------------------------------------------------------------------------

"""
P-1.31 Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
"""

def make_change(amount_charged, amount_given):

    """
    Return the number of each kind of bill and coin to give back as change.
    """
    
    assert amount_given >= amount_charged, "Amount given must be greater than or equal to amount charged."
    
    change = amount_given - amount_charged
    denominations = [10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1]  # Denominations in cents
    denomination_names = ["$100 bill", "$50 bill", "$20 bill", "$10 bill", "$5 bill", "$1 bill", "Quarter", "Dime", "Nickel", "Penny"]
    
    change_in_cents = int(round(change * 100))  # Convert change to cents
    result = {}
    
    for denom, name in zip(denominations, denomination_names):
        count = change_in_cents // denom  # Determine how many of this denomination
        if count > 0:
            result[name] = count
            change_in_cents -= count * denom  # Reduce the remaining change
    
    return result

# --------------------------------------------------------------------------------------------

"""
P-1.32 Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =
,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
"""

def simple_calculator():

    """
    Simulate a simple calculator using console input and output.
    """
    
    total = 0
    current_input = ''
    operator = '+'
    
    print("Simple Calculator. Enter numbers and operators (+, -, *, /). Type '=' to get the result or 'exit' to quit.")
    
    while True:
        user_input = input("Enter number or operator: ")
        
        if user_input.lower() == 'exit':
            print("Exiting calculator.")
            break
        
        if user_input == '=':
            print(f"Result: {total}")
            total = 0  # Reset total for new calculation
            operator = '+'
            continue
        
        if user_input in ['+', '-', '*', '/']:
            operator = user_input
            continue
        
        try:
            number = float(user_input)
            
            if operator == '+':
                total += number
            elif operator == '-':
                total -= number
            elif operator == '*':
                total *= number
            elif operator == '/':
                if number != 0:
                    total /= number
                else:
                    print("Error: Division by zero.")
                    continue
            
            print(f"Current total: {total}")
        
        except ValueError:
            print("Invalid input. Please enter a number or an operator.")


# --------------------------------------------------------------------------------------------

"""
P-1.33 Write a Python program that simulates a handheld calculator. Your pro-
gram should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each op-
eration is performed. Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation.
"""

def handheld_calculator():

    """
    Simulate a handheld calculator using console input and output.
    """
    
    total = 0
    current_input = ''
    operator = '+'
    
    print("Handheld Calculator. Enter numbers and operators (+, -, *, /). Type 'C' to clear, '=' to get the result, or 'exit' to quit.")
    
    while True:
        user_input = input("Enter number or operator: ")
        
        if user_input.lower() == 'exit':
            print("Exiting calculator.")
            break
        
        if user_input.upper() == 'C':
            total = 0
            operator = '+'
            print("Calculator cleared.")
            continue
        
        if user_input == '=':
            print(f"Result: {total}")
            total = 0  # Reset total for new calculation
            operator = '+'
            continue
        
        if user_input in ['+', '-', '*', '/']:
            operator = user_input
            continue
        
        try:
            number = float(user_input)
            
            if operator == '+':
                total += number
            elif operator == '-':
                total -= number
            elif operator == '*':
                total *= number
            elif operator == '/':
                if number != 0:
                    total /= number
                else:
                    print("Error: Division by zero.")
                    continue
            
            print(f"Current total: {total}")
        
        except ValueError:
            print("Invalid input. Please enter a number or an operator.")


# --------------------------------------------------------------------------------------------

"""
P-1.34 A common punishment for school children is to write out a sentence mul-
tiple times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.
"""

def introduce_typo(sentence):

    """
    Introduce a random typo into the given sentence.
    """
    import random
    
    sentence_list = list(sentence)
    typo_index = random.randint(0, len(sentence_list) - 1)
    
    while not sentence_list[typo_index].isalpha():
        typo_index = random.randint(0, len(sentence_list) - 1)
    sentence_list[typo_index] = random.choice('abcdefghijklmnopqrstuvwxyz')
    
    return ''.join(sentence_list)


def write_sentences_with_typos():

    """
    Write out the sentence "I will never spam my friends again." one hundred times with random typos.
    """
    import random
    
    sentence = "I will never spam my friends again."
    typo_indices = random.sample(range(100), 8)  # Select 8 unique indices for typos
    
    for i in range(100):
        if i in typo_indices:
            typo_sentence = introduce_typo(sentence)
            print(f"{i + 1}: {typo_sentence}")
        else:
            print(f"{i + 1}: {sentence}")


# --------------------------------------------------------------------------------------------

"""
P-1.35 The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20,...,100.
"""

def has_duplicate_birthdays(birthdays):

    """
    Return True if there are duplicate birthdays in the list, False otherwise.
    """
    
    return len(birthdays) != len(set(birthdays))  # Compare length of list with length of set of birthdays
def test_birthday_paradox():

    """
    Test the birthday paradox for n = 5, 10, 15, ..., 100.
    """
    import random
    
    for n in range(5, 101, 5):
        trials = 1000
        duplicate_count = 0
        
        for _ in range(trials):
            birthdays = [random.randint(1, 365) for _ in range(n)]  # Generate n random birthdays
            if has_duplicate_birthdays(birthdays):
                duplicate_count += 1
        
        probability = duplicate_count / trials
        print(f"Number of people: {n}, Probability of shared birthday: {probability:.4f}")

# --------------------------------------------------------------------------------------------

"""
P-1.36 Write a Python program that inputs a list of words, separated by white-
space, and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book.
"""

def count_word_frequencies(word_list):

    """
    Return a dictionary with the frequency of each word in the word_list.
    """
    
    frequency = {}
    
    for word in word_list:
        word = word.lower()  # Convert to lowercase for uniformity
        if word in frequency:
            frequency[word] += 1  # Increment count if word already exists
        else:
            frequency[word] = 1  # Initialize count for new word
    
    return frequency

# ======= END OF FILE =======