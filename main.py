import requests
API_KEY = open("api_key.txt").read()

with open("list.csv") as f:
    for line in f:
        line_split = line.split(",")
        address = line_split[0]
        name = line_split[1]
        full_address = f"{address}, barcelona"

        response = requests.get(f"https://maps.googleapis.com/maps/api/geocode/json?address={full_address}&key={API_KEY}")

        json = response.json()
        location = response.json()["results"][0]["geometry"]["location"]
        lat = location["lat"]
        lon = location["lng"]

        print(f"{lat}, {lon}, {name}")
