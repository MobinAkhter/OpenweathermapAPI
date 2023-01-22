import requests
# For safety reasons, generated another API key, this one no longer works.
# Could have used env variable for API_KEY but meh
API_KEY = "0bee562efca47fd12a5aa60956b77894"

city = input("Enter a city name: ")
request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("Error! Try again in a bit and/or try other cities")