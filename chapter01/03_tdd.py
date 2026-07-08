import unittest

def main():
    """
    This is the main function that takes two numbers from the command line arguments,
    multiplies them using the multiply function, and prints the result.
    """
    import sys
    num1, num2 = sys.argv[1:]
    num1, num2 = int(num1), int(num2)
    print(multiply(num1, num2))

def multiply(num1, num2):
    """
    Multiply two numbers using repeated addition.
    This is an example of a sociable unit
    it has a dependency on the addition unit and cannot be tested in isolation.
    """
    total = 0
    for _ in range(num2):
        total = addition(total, num1)
    return total

def addition(*args):
    """
    Add any number of numbers together.
    This is an example of a solitary unit
    it has no dependencies on other units and can be tested in isolation.
    """
    total = 0;
    for num in args:
        total += num
    return total

class AdditionTestCase(unittest.TestCase):
    def test_addition(self):
        """
        Basic addition test
        """
        result = addition(2, 3);
        assert result == 5, f"Expected 5 but got {result}"
    def test_threeargs(self):
        """
        Test addition with three arguments
        """
        result = addition(2, 3, 4)
        assert result == 9, f"Expected 9 but got {result}"
    def test_noargs(self):
        """
        Test addition with no arguments
        """
        result = addition()
        assert result == 0, f"Expected 0 but got {result}"
 
if __name__ == '__main__':
    unittest.main()