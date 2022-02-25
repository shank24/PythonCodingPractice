import unittest
from datetime import *

class CreditCardValidationTest(unittest.Testcase):

    def test_validateCard_valid(self):
        result = validateCard(date(2018,2,2))
        self.assertEqual('Valid',result)

if __name__=='__main__':
    unittest.main()
