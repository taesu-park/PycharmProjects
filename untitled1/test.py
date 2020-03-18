import requests, json, pprint

data={'nickname':'대전2반박태수', 'yourAnswer':'kubernetes'}
headers = {"Accept": "application/json", "Content-Type": "application/json"}

r = requests.post('http://13.125.222.176/quiz/jordan',headers=headers, data=json.dumps(data))
pprint.pprint(r.json())