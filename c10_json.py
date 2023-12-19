from pathlib import Path
import json
numbers = [2, 3, 5, 7, 11, 13]
path = Path('c10_json.json')
contents = json.dumps(numbers)
path.write_text(contents)

path = Path('c10_json.json')
contents = path.read_text()
numbers = json.loads(contents)
# print(numbers)

username = input("What is your name? ")
path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)
print(f"We'll remember you when you come back, {username}!")