person_0 = {"first_name": "israel", "last_name": "mendoza", "age": 27, "gender": "male"}
person_1 = dict(first_name="margarita", last_name="mendoza", gender="female")


person_0["user ID"] = "imendoza"

print(person_0.get("location", None))

if 'location' in person_0.keys():
	print(person_0['location'])
else:
	print("There is no location in person_0")


try:
	print(person_1["age"])
except KeyError:
	print("There is no 'age' in person_1")