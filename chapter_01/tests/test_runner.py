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



# Run the birthday paradox test
test_birthday_paradox()