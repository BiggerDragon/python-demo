import unittest
import re

# print(help(unittest))

class TestUtilsFunctions(unittest.TestCase):

    def test_is_correct_id_no(self):
        self.assertEqual(is_correct_id_no(""), False)
        self.assertTrue(is_correct_id_no("411524199507037213"))


def is_correct_id_no(id_no):
    """Tell if the given id no is correct!
    >>> is_correct_id_no("000")
    False
    >>> is_correct_id_no("")
    False
    >>> is_correct_id_no("411524199507037213")
    True
    >>> is_correct_id_no("YYsssYYYuu12345678")
    False
    """
    reg = "[0-9]{17}[xX0-9]"
    if re.match(reg, id_no):
        return True
    else:
        return False

if __name__ == "__main__":
    unittest.main()
