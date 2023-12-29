import unittest
from src.name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    def test_first_last_name(self) -> None:
        """Do names like 'Janis Joplin' work?"""
        formatted_name: str = get_formatted_name("janis", "joplin")
        self.assertEqual("Janis Joplin", formatted_name)

    def test_first_last_middle_name(self) -> None:
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name: str = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual("Wolfgang Amadeus Mozart", formatted_name)


if __name__ == "__main__":
    unittest.main()