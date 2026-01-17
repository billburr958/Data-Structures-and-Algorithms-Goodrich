import unittest
import sys
import os

# Add parent directory to path to import solutions
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solutions import *


class TestReinforcementExercises(unittest.TestCase):
    """Tests for Reinforcement exercises (R-1.1 to R-1.12)"""

    # R-1.1
    def test_is_multiple(self):
        self.assertTrue(is_multiple(10, 5))
        self.assertTrue(is_multiple(20, 4))
        self.assertTrue(is_multiple(0, 5))
        self.assertFalse(is_multiple(10, 3))
        self.assertFalse(is_multiple(7, 2))
        self.assertFalse(is_multiple(5, 0))  # Division by zero case

    # R-1.2
    def test_is_even(self):
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(100))
        self.assertTrue(is_even(-4))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(99))
        self.assertFalse(is_even(-3))

    def test_is_even_alternative(self):
        self.assertTrue(is_even_alternative(0))
        self.assertTrue(is_even_alternative(2))
        self.assertTrue(is_even_alternative(100))
        self.assertTrue(is_even_alternative(-4))
        self.assertFalse(is_even_alternative(1))
        self.assertFalse(is_even_alternative(99))

    # R-1.3
    def test_minmax(self):
        self.assertEqual(minmax([3, 1, 4, 1, 5, 9, 2, 6]), (1, 9))
        self.assertEqual(minmax([5]), (5, 5))
        self.assertEqual(minmax([10, 20, 30]), (10, 30))
        self.assertEqual(minmax([-5, -1, -10]), (-10, -1))

    # R-1.4
    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares(1), 0)  # No positive integers smaller than 1
        self.assertEqual(sum_of_squares(2), 1)  # 1^2 = 1
        self.assertEqual(sum_of_squares(3), 5)  # 1^2 + 2^2 = 5
        self.assertEqual(sum_of_squares(5), 30)  # 1 + 4 + 9 + 16 = 30

    # R-1.5
    def test_sum_of_squares_inbuilt(self):
        self.assertEqual(sum_of_squares_inbuilt(1), 0)
        self.assertEqual(sum_of_squares_inbuilt(2), 1)
        self.assertEqual(sum_of_squares_inbuilt(3), 5)
        self.assertEqual(sum_of_squares_inbuilt(5), 30)

    # R-1.6
    def test_sum_of_squares_odd(self):
        self.assertEqual(sum_of_squares_odd(1), 0)  # No odd positive integers smaller than 1
        self.assertEqual(sum_of_squares_odd(2), 1)  # 1^2 = 1
        self.assertEqual(sum_of_squares_odd(4), 10)  # 1^2 + 3^2 = 10
        self.assertEqual(sum_of_squares_odd(6), 35)  # 1 + 9 + 25 = 35

    # R-1.7
    def test_sum_of_squares_odd_inbuilt(self):
        self.assertEqual(sum_of_squares_odd_inbuilt(1), 0)
        self.assertEqual(sum_of_squares_odd_inbuilt(2), 1)
        self.assertEqual(sum_of_squares_odd_inbuilt(4), 10)
        self.assertEqual(sum_of_squares_odd_inbuilt(6), 35)

    # R-1.8
    def test_negative_index_equivalent(self):
        s = "hello"
        self.assertEqual(negative_index_equivalent(s, -1), 4)
        self.assertEqual(negative_index_equivalent(s, -2), 3)
        self.assertEqual(negative_index_equivalent(s, -5), 0)

    # R-1.9
    def test_generate_range(self):
        result = list(generate_range())
        self.assertEqual(result, [50, 60, 70, 80])

    # R-1.10
    def test_generate_reverse_range(self):
        result = list(generate_reverse_range())
        self.assertEqual(result, [8, 6, 4, 2, 0, -2, -4, -6, -8])

    # R-1.11
    def test_generate_powers_of_two(self):
        result = generate_powers_of_two()
        self.assertEqual(result, [1, 2, 4, 8, 16, 32, 64, 128, 256])

    # R-1.12
    def test_random_choice(self):
        data = [1, 2, 3, 4, 5]
        for _ in range(10):
            result = random_choice(data)
            self.assertIn(result, data)


class TestCreativityExercises(unittest.TestCase):
    """Tests for Creativity exercises (C-1.13 to C-1.28)"""

    # C-1.13
    def test_reverse_list(self):
        self.assertEqual(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])
        self.assertEqual(reverse_list([5]), [5])
        self.assertEqual(reverse_list([1, 2]), [2, 1])

    # C-1.14
    def test_has_odd_product_pair(self):
        self.assertTrue(has_odd_product_pair([1, 3, 5]))  # Multiple odd numbers
        self.assertTrue(has_odd_product_pair([2, 3, 5]))  # At least two odd
        self.assertFalse(has_odd_product_pair([2, 4, 6]))  # No odd numbers
        self.assertFalse(has_odd_product_pair([2, 3]))  # Only one odd

    # C-1.15
    def test_all_distinct(self):
        self.assertTrue(all_distinct([1, 2, 3, 4]))
        self.assertFalse(all_distinct([1, 2, 3, 1]))
        self.assertTrue(all_distinct([5]))

    def test_all_distinct_alternative(self):
        self.assertTrue(all_distinct_alternative([1, 2, 3, 4]))
        self.assertFalse(all_distinct_alternative([1, 2, 3, 1]))
        self.assertTrue(all_distinct_alternative([5]))

    # C-1.18
    def test_generate_custom_list(self):
        result = generate_custom_list()
        self.assertEqual(result, [0, 2, 6, 12, 20, 30, 42, 56, 72, 90])

    # C-1.19
    def test_generate_alphabet_list(self):
        result = generate_alphabet_list()
        expected = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.assertEqual(result, expected)

    # C-1.20
    def test_shuffle(self):
        data = [1, 2, 3, 4, 5]
        original = data.copy()
        shuffle(data)
        # Check that all elements are still present
        self.assertEqual(sorted(data), sorted(original))

    # C-1.22
    def test_dot_product(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        result = dot_product(a, b)
        self.assertEqual(result, [4, 10, 18])

    def test_dot_product_alternative(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        result = dot_product_alternative(a, b)
        self.assertEqual(result, [4, 10, 18])

    # C-1.24
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("HELLO"), 2)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("bcdfg"), 0)
        self.assertEqual(count_vowels(""), 0)

    # C-1.25
    def test_remove_punctuation(self):
        self.assertEqual(remove_punctuation("Let's try, Mike."), "Lets try Mike")
        self.assertEqual(remove_punctuation("Hello!"), "Hello")
        self.assertEqual(remove_punctuation("No punctuation"), "No punctuation")

    def test_remove_punctuation_alternative(self):
        self.assertEqual(remove_punctuation_alternative("Let's try, Mike."), "Lets try Mike")
        self.assertEqual(remove_punctuation_alternative("Hello!"), "Hello")

    # C-1.26
    def test_check_arithmetic_formulas(self):
        self.assertEqual(check_arithmetic_formulas(3, 2, 5), "3 + 2 = 5")
        self.assertEqual(check_arithmetic_formulas(5, 2, 3), "5 - 2 = 3")
        self.assertEqual(check_arithmetic_formulas(3, 4, 12), "3 * 4 = 12")
        self.assertEqual(check_arithmetic_formulas(10, 2, 5), "10 / 2 = 5")

    def test_check_arithmetic_formulas_alternative(self):
        self.assertEqual(check_arithmetic_formulas_alternative(3, 2, 5), "3 + 2 = 5")
        self.assertEqual(check_arithmetic_formulas_alternative(5, 2, 3), "5 - 2 = 3")

    # C-1.27
    def test_generate_factors_in_order(self):
        result = list(generate_factors_in_order(12))
        self.assertEqual(result, [1, 2, 3, 4, 6, 12])

        result = list(generate_factors_in_order(100))
        self.assertEqual(result, [1, 2, 4, 5, 10, 20, 25, 50, 100])

    # C-1.28
    def test_norm(self):
        self.assertAlmostEqual(norm([3, 4]), 5.0)  # Euclidean norm
        self.assertAlmostEqual(norm([1, 1, 1]), 1.732050807568877, places=5)
        self.assertAlmostEqual(norm([3, 4], 1), 7.0)  # Manhattan norm
        self.assertAlmostEqual(norm([3, 4], 2), 5.0)  # Euclidean norm


class TestProjectExercises(unittest.TestCase):
    """Tests for Project exercises (P-1.29 to P-1.36)"""

    # P-1.29
    def test_generate_permutations(self):
        result = generate_permutations(['a', 'b', 'c'])
        self.assertEqual(len(result), 6)  # 3! = 6
        self.assertIn('abc', result)
        self.assertIn('cba', result)

    def test_generate_permutations_alternative(self):
        result = generate_permutations_alternative(['a', 'b', 'c'])
        self.assertEqual(len(result), 6)
        self.assertIn('abc', result)
        self.assertIn('cba', result)

    # P-1.30
    def test_count_divisions_by_two(self):
        self.assertEqual(count_divisions_by_two(8), 3)  # 8 -> 4 -> 2 -> 1
        self.assertEqual(count_divisions_by_two(10), 3)  # 10 -> 5 -> 2.5 -> 1.25
        self.assertEqual(count_divisions_by_two(3), 1)  # 3 -> 1.5

    # P-1.31
    def test_make_change(self):
        result = make_change(3.50, 5.00)
        total_change = sum(count * denomination for count, denomination in
                          [(result.get('$1 bill', 0), 100),
                           (result.get('Quarter', 0), 25),
                           (result.get('Dime', 0), 10),
                           (result.get('Nickel', 0), 5)])
        self.assertEqual(total_change, 150)  # $1.50 in cents

    # P-1.35
    def test_has_duplicate_birthdays(self):
        self.assertTrue(has_duplicate_birthdays([1, 2, 3, 1]))
        self.assertFalse(has_duplicate_birthdays([1, 2, 3, 4]))
        self.assertTrue(has_duplicate_birthdays([100, 200, 100]))

    # P-1.36
    def test_count_word_frequencies(self):
        words = ["hello", "world", "hello", "python"]
        result = count_word_frequencies(words)
        self.assertEqual(result['hello'], 2)
        self.assertEqual(result['world'], 1)
        self.assertEqual(result['python'], 1)


def run_tests():
    """Run all tests and display results"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestReinforcementExercises))
    suite.addTests(loader.loadTestsFromTestCase(TestCreativityExercises))
    suite.addTests(loader.loadTestsFromTestCase(TestProjectExercises))

    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Print summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print("="*70)

    return result


if __name__ == '__main__':
    run_tests()
