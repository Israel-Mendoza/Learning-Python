import unittest
from src.phonebook import Phonebook


class PhonebookTest(unittest.TestCase):

    def setUp(self) -> None:  # This will run before each test
        self.phonebook = Phonebook()

    def tearDown(self) -> None:  # This will run after each test
        pass

    def test_lookup_by_name(self) -> None:
        self.phonebook.add("Bob", "12345")
        number: str = self.phonebook.lookup("Bob")
        self.assertEqual(number, "12345")

    def test_missing_name(self) -> None:
        self.phonebook = Phonebook()
        with self.assertRaises(KeyError):
            self.phonebook.lookup("Missing")

    def test_empty_phonebook_is_consistent(self) -> None:
        self.phonebook = Phonebook()
        self.assertTrue(self.phonebook.is_consistent)

    def test_is_consistent_with_single_entry(self) -> None:
        self.phonebook.add("Bob", "12345")
        self.assertTrue(self.phonebook.is_consistent)

    def test_is_consistent_with_different_entries(self) -> None:
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Anna", "54321")
        self.assertTrue(self.phonebook.is_consistent)

    def test_is_not_consistent_with_repeated_phone_numbers(self) -> None:
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Charlie", "12345")  # Identical to another phone number (Bob's)
        self.assertFalse(self.phonebook.is_consistent)

    def test_is_not_consistent_with_repeated_phone_number_prefix(self) -> None:
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Charlie", "123")  # Prefix to another phone number (Bob's)
        self.assertFalse(self.phonebook.is_consistent)

    def test_is_not_consistent_with_repeated_phone_number_prefix2(self) -> None:
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Charlie", "1234567")
        self.assertFalse(self.phonebook.is_consistent)

    @unittest.skip("This is how you skip a test")
    def test_nothing_to_test_here(self):
        pass
