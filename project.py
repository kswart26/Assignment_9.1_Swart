import requests

#Function to get weather info from openweathermap
def weather_info(query):
   api_key = "e4e9aaae0f71d932bfeff02a701551b3"
   base_url = "http://api.openweathermap.org/data/2.5/weather?"
   complete_url = base_url + "appid=" + api_key + "&" + query
   res=requests.get(complete_url);
   return res.json();

#Function to display weather info
def display_results(weathers,city):
   print("Wind velocity: {} m/s".format(weathers['wind']['speed']))   
   print("Temperature: {} degrees Kelvin".format(weathers['main']['temp']))
   print("Weather: {}".format(weathers['weather'][0]['main']))
   print("Description: {}".format(weathers['weather'][0]['description']))

#Main function
def main():
   
   # Get city name from user
   city=input('Enter city name:')
   print()
   
   try:
      query='q='+city;
      w_data=weather_info(query);
      display_results(w_data, city)
      print()
   except:
      print('City under that name not found, please try again. ')

#Starting the program
if __name__=='__main__':
   main()