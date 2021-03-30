# import python_weather
# s =  input("Enter the city name you want to fetch weather for:\t")
# client = python_weather.Client(format=python_weather.IMPERIAL)
# weather = await client.find(s)
# print("Current Temperature:\t",weather.current.temperature)
# print("\nForecast:")
# for forecast in weather.forecast:
#     print("Date: ", str(forecast.date)+"\t:", forecast.sky_text, forecast.temperature)

# # close the wrapper once done
# await client.close()

import python_weather
import asyncio
# declare the client. format defaults to metric system (celcius, km/h, etc.)
client = python_weather.Client(format=python_weather.IMPERIAL)

# fetch a weather forecast from a city
loop = asyncio.get_event_loop()
weather = loop.run_until_complete( client.find("Washington DC") )
loop.close()

# returns the current city temperature (int)
print(weather.current.temperature)

# get the weather forecast for a few days
for forecast in weather.forecast:
    print(str(forecast.date), forecast.sky_text, forecast.temperature)

# close the wrapper once done
loop = asyncio.get_event_loop()
loop.run_until_complete( client.close())
loop.close()