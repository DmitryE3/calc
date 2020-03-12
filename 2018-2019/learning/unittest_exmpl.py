"""Разработайте юнит-тесты проверяющие корректность работы функции. Удалось ли найти какие-либо дефекты в этой функции,
полагаясь на ее назначение исходя из описания? Учтите, что вопрос не на знание фреймворков тестирования и их применение,
можете взять любой, или даже разработать ряд самостоятельных функций. function isEven(number) {
// Returns True if **number** is even or False if it is odd.
return number % 2;
}
"""


def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


import unittest


class ExmplTest(unittest.TestCase):
    def test_isEven(self):
        self.assertTrue(isEven(2))
        self.assertFalse(isEven(3))


if __name__ == '__main__':
    unittest.main()
