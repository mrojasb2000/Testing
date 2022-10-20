import unittest
from fibo import fibonacci

# 1 1 2 3 5 8 13 21 34 55


class Test(unittest.TestCase):
    def test_should_return_5_when_pass_4(self):
        result = fibonacci(4)
        self.assertEqual(result, 5)

    def test_should_return_1_when_pass_0(self):
        expected = 1
        received = fibonacci(0)
        self.assertAlmostEqual(received, expected)

    def test_should_return_1_when_pass_1(self):
        expected = 1
        received = fibonacci(1)
        self.assertAlmostEqual(received, expected)

    def test_should_return_err_when_pass_not_number(self):
        expected = 'Error: input type is not number'
        received = fibonacci(1)
        self.assertAlmostEqual(received, expected)


if __name__ == "__main__":
    unittest.main()
