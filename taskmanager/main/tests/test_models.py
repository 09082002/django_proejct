from random import randint

from django.test import TestCase


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once too set up non-modified data for all class methods")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertTrue(False)

    def test_false_is_true(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_seven_plus_eight_equals_fifteen(self):
        print("Method: test_seven_plus_eight_equals_fifteen")
        self.assertEqual(7 + 8, 15)

    def test_years(self):
        def get_years():
            return randint(2020, 2024)

        print("Method: Now")
        self.assertEqual(2022, get_years())

    def test_positive_check(self):
        testValue = 20
        def message():
            return randint(18, 25)
        self.assertTrue(testValue, message())

    # def test_cheaks(self):
    #     def get_years():
    #         return randint(2020, 2024)
    #
    #     print("Method: Now")
    #     self.assertEqual(2022, get_years())

    # def test_equal(self):
    #     def app():
    #         return randint(5, 10)
    #     print("Method: test_equal")
    #     self.assertEqual(2 * 3, app())
