import unittest

import ccval
from ccval import hasnumbers


class TestSum(unittest.TestCase):
    def test_hasnumber(self):
        data = "4563838383838388"
        result = hasnumbers(data)
        self.assertEqual(result, True)

    def test_nothasnumber(self):
        data = "abcdefg"
        result = hasnumbers(data)
        self.assertEqual(result, False)

    def test_startwith4(self):
        data = "45"
        result = ccval.startwith(data)
        self.assertEqual(result, True)

    def test_startwith5(self):
        data = "55"
        result = ccval.startwith(data)
        self.assertEqual(result, True)

    def test_startwith6(self):
        data = "65"
        result = ccval.startwith(data)
        self.assertEqual(result, True)

    def test_startwith37(self):
        data = "3765"
        result = ccval.startwith(data)
        self.assertEqual(result, True)

    def test_startwith34(self):
        data = "3465"
        result = ccval.startwith(data)
        self.assertEqual(result, True)

    def test_startwith35(self):
        data = "3565"
        result = ccval.startwith(data)
        self.assertEqual(result, True)

    def test_luhn_check(self):
        data = "79927398713"
        result = ccval.luhn_check(data)
        self.assertEqual(result, True)


if __name__ == "__main__":
    unittest.main()
    print("Completed all test Successfully")
