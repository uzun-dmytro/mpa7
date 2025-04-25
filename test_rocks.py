import unittest
import io
import sys
from rocks import min_operations_to_squares, is_perfect_square, min_cost_to_square

class TestRocks(unittest.TestCase):
    def test_is_perfect_square(self):
        self.assertTrue(is_perfect_square(1))
        self.assertTrue(is_perfect_square(4))
        self.assertTrue(is_perfect_square(9))
        self.assertFalse(is_perfect_square(2))
        self.assertFalse(is_perfect_square(5))
        self.assertFalse(is_perfect_square(8))

    def test_min_cost_to_square(self):
        self.assertEqual(min_cost_to_square(3), 1)  # 3 → 4 (1)
        self.assertEqual(min_cost_to_square(5), 1)  # 5 → 4 (1)
        self.assertEqual(min_cost_to_square(8), 1)  # 8 → 9 (1)
        self.assertEqual(min_cost_to_square(10), 1) # 10 → 9 (1)
        self.assertEqual(min_cost_to_square(15), 1) # 15 → 16 (1)

    def test_min_operations_to_squares(self):
        # Тестовий випадок з умови
        input_data = "4\n3 5 4 10\n"
        expected_output = "1"
        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        sys.stdin = io.StringIO(input_data)
        min_operations_to_squares()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

        # Додаткові тестові випадки
        test_cases = [
            ("2\n1 2\n", "0"),  # Вже правильна кількість
            ("2\n3 5\n", "1"),   # Один з двох має стати квадратом
            ("4\n0 0 0 0\n", "4"), # Всі нулі → потрібно 2 операції на кожен
            ("6\n1 2 3 4 5 6\n", "1"), # Вже 2 квадрати, потрібно ще 1
            ("4\n10 11 12 13\n", "3") # Оновлений тестовий випадок
        ]
        
        for input_data, expected_output in test_cases:
            with self.subTest(input_data=input_data):
                captured_output = io.StringIO()
                sys.stdout = captured_output
                sys.stdin = io.StringIO(input_data)
                min_operations_to_squares()
                sys.stdout = sys.__stdout__
                self.assertEqual(captured_output.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()