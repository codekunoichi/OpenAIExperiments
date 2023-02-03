import json

# JSON data
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Parsing JSON data using json.loads()
parsed_data = json.loads(json_data)

# Accessing values in the parsed data
print("Name: ", parsed_data["name"])
print("Age: ", parsed_data["age"])
print("City: ", parsed_data["city"])
