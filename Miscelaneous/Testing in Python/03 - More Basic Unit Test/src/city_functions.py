def city_country_name(city_name: str, country_name: str, population: int = 0) -> str:
    formatted_city: str = f"{city_name.title()}, {country_name.title()}"
    if population:
        return f"{formatted_city} - population: {population}"
    return formatted_city
