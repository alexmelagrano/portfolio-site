import unittest


class FoodTests(unittest.TestCase):

    def testFood(self):
        self.assertEquals('food'.upper(), 'FOOD')


def main():
    unittest.main()

if __name__ == '__main__':
    main()
