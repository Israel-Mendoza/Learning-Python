from pydantic import BaseModel
from datetime import date


class Automobile(BaseModel):
    manufacturer: str
    series_name: str
    type_: str
    is_electric: bool = False
    manufactured_date: date
    base_msrp_usd: float
    vin: str
    number_of_doors: int = 4
    registration_country: str | None = None
    license_plate: str | None = None


incoming_data_dict = {
    "manufacturer": "Volkswagen",
    "series_name": "New Vocho",
    "type_": "Vocho",
    "manufactured_date": date.fromisoformat("2020-12-12"),
    "base_msrp_usd": 1.111,
    "vin": "123AAA",
    "registration_country": "Mexico"
}

incoming_data_json = """
{
    "manufacturer": "Volkswagen",
    "series_name": "New Vocho",
    "type_": "Vocho",
    "is_electric": false,
    "manufactured_date": "2020-12-12",
    "base_msrp_usd": 1.111,
    "vin": "123AAA",
    "number_of_doors": 4,
    "registration_country": "Mexico",
    "license_plate": null
}
"""

# Deserializing the objects
a_model_from_dict = Automobile.model_validate(incoming_data_dict)
a_model_from_json = Automobile.model_validate_json(incoming_data_json)

print(a_model_from_dict == a_model_from_json)
# True

# Serializing and deserializing the models
a_model_from_dict = Automobile.model_validate(a_model_from_dict.model_dump())
a_model_from_json = Automobile.model_validate_json(a_model_from_json.model_dump_json(indent=4))

print(a_model_from_dict == a_model_from_json)
# True
