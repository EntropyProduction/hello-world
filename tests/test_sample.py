"""A minimal Python test example using the standard library."""

import unittest


class SampleTest(unittest.TestCase):
    def test_addition(self) -> None:
        self.assertEqual(1 + 1, 2)


if __name__ == "__main__":
    unittest.main()
