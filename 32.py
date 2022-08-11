import requests
response = requests.post("http://localhost:5001/whatismyname")
expected = "save new car"
actual = response.text
print(response.text)
assert expected == actual