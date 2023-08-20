import requests
import key

city = input('Enter city name: ')
request_url = f'{key.BASE_URL}?appid={key.API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    #print(data)
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    
    print('Weather: ', weather)
    print('Temperature: ', temperature, 'celsius') 
else:
    print('An erroe occurred.')
