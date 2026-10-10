import json 

filename = 'data.json'

try:
    with open(filename, "r") as file:
        data = json.load(file)

    print("Formatted JSON Data:")
    print(json.dumps(data, indent=4))

except FileNotFoundError:
    print("JSON File not found!")

except json.JSONDecodeError:
    print("Invalid JSON format!")