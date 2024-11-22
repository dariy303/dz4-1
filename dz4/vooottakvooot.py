import unittest
def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as e:
            print(f'We have problems {e}')
        else:
            print(f'No problems. Result - {result}')
    return checker

# по задуму якщо програма працює то 3 теста має бути зафейлено, якщо 4 то вона просто не працює
class my_test(unittest.TestCase):
        def test_args(self):
            self.assertEqual((x3), '/')
        def test_args1(self):
            self.assertEqual((x3), '+')
        def test_args2(self):
            self.assertEqual((x3), '-')
        def test_args3(self):
            self.assertEqual((x3), '*')

def calculate(expression):
 return eval(expression)
calculate = checker(calculate)
x = int(input('Перше число: '))
x2 = int(input('Другое число: '))
x3 = (input('Дія: '))
if x3 == '+':
    calculate('x+x2')
elif x3 == '-':
    calculate('x-x2')
elif x3 == '*':
    calculate('x*x2')
elif x3 == '/':
    calculate('x/x2')