import requests,json,os

key=os.getenv("weather")
print(key)

if not key:
    print('Error')
    exit()

city =input("Enter the city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

response = requests.get(url)
#print(response)
result=response.json()

# with open("weather.json",'w+') as file:
#     json.dump(result,file,indent=4)
    
# with open("weather.json", 'r') as file:
#     data = json.load(file)    
    
celsius = result["main"]["temp"] - 273.15
print(f"{city}\'s temperature is {celsius:.2f}°C")
print(f"{city}\'s humidity is {result["main"]["humidity"]}")
print(f"{city}\'s pressure is {result["main"]["pressure"]}")
print(f"{city}\'s wind speed is {result["wind"]["speed"]} Km/Hr")


