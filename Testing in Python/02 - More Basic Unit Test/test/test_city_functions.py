import unittest
from src.city_functions import city_country_name


class CityCountryStringTest(unittest.TestCase):

    def test_correct_city_format_when_lower_case(self) -> None:
        formatted_city_name: str = city_country_name("mexico city", "mexico")
        self.assertEqual(formatted_city_name, "Mexico City, Mexico")

    def test_correct_city_format_when_upper_case(self) -> None:
        formatted_city_name: str = city_country_name("MEXICO CITY", "MEXICO")
        self.assertEqual(formatted_city_name, "Mexico City, Mexico")

    def test_correct_city_format_and_population_when_lower_case(self) -> None:
        formatted_city_name: str = city_country_name("mexico city", "mexico", 23_000_000)
        self.assertEqual(formatted_city_name, "Mexico City, Mexico - population: 23000000")

    def test_correct_city_format_and_population_when_upper_case(self) -> None:
        formatted_city_name: str = city_country_name("MEXICO CITY", "MEXICO", 23_000_000)
        self.assertEqual(formatted_city_name, "Mexico City, Mexico - population: 23000000")


if __name__ == "__main__":
    unittest.main()
