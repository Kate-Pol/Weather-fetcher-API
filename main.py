import requests
import key
import datetime as dt


city = input('Enter city name: ')
request_url = f'{key.BASE_URL}?appid={key.API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    #print(data)
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    humidity = data['main']['humidity']
    sunrise_time = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])
    wind_speed = data['wind']['speed']
    
    print('Weather: ', weather)
    print('Temperature: ', temperature, 'celsius') 
    print('Humidity: ', humidity)
    print('Sunrize time is: ', sunrise_time)
    print('Sunset time is: ', sunset_time)
    print('Wind speed: ', wind_speed)
else:
    print('An erroe occurred.')
