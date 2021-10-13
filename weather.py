import requests

def get_weather_desc_and_temp():
    api_key="3afd8bdec31ac41b21c59226bdaa33fe"
    city="Singapore"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"
    #print(url)

    #get weather data
    request = requests.get(url)
    json = request.json()
    #print(json) 

    #get data from returned json values
    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return { 'description':description,'temp_min':temp_min,'temp_max':temp_max}

def main():
    #print the results 
    weather_dict = get_weather_desc_and_temp()
    print("Today's forecast is",weather_dict.get('description'))
    print("The minimum temperature is",weather_dict.get('temp_min'))
    print("The maximum temperature is",weather_dict.get('temp_max'))


main()