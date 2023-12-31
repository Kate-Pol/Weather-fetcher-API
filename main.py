import requests
import key
import datetime as dt
from tkinter import *
import math



city = input('Enter city name: ')
request_url = f'{key.BASE_URL}?appid={key.API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp'] - 273.15, 2)
    humidity = data['main']['humidity']
    sunrise_time = dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])
    wind_speed = data['wind']['speed']
    
    print('Weather: ', weather)
    print('Temperature: ', temperature, 'celsius') 
    print('Humidity: ', humidity)
    print('Sunrize time is: ', sunrise_time, 'local time')
    print('Sunset time is: ', sunset_time, 'local time')
    print('Wind speed: ', wind_speed, 'm/s')
else:
    print('An erroe occurred.')
    
    
    
root = Tk()
root.geometry('500x400')
root.title(f'{city} Weather')


def display_city(city):
	city_label = Label(root, text = f'{city}')
	city_label.config(font=('Consolas', 28))
	city_label.pack(side='top')

def display_weather():
	weath = Label(root, text=f"Weather: {weather}")
	weath.config(font=('Consolas', 15))
	weath.pack(side='top')
	
	temp = Label(root, text=f'Temperature: {temperature} celsius' )
	temp.config(font=('Consolas', 15))
	temp.pack(side='top')
	
	humid = Label(root, text=f'Humidity: {humidity}' )
	humid.config(font=('Consolas', 15))
	humid.pack(side='top')
	
	sunrise = Label(root, text=f'Sunrise time: {sunrise_time}')
	sunrise.config(font=('Consolas', 15))
	sunrise.pack(side='top')
	
	sunset = Label(root, text=f'Sunset time: {sunset_time}')
	sunset.config(font=('Consolas', 15))
	sunset.pack(side='top')
	
	wind = Label(root, text=f'Wind speed: {wind_speed}')
	wind.config(font=('Consolas', 15))
	wind.pack(side='top')


display_city(city)
display_weather()
root.mainloop()
    
    
