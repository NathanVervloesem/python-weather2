from dotenv import load_dotenv
from pprint import pprint
import requests
import os

# Loading a new environemnt
# py -m venv .venv
# py -m .venv/Scripts/activate

load_dotenv()  # Loading the API_KEY, something wrong here


def get_current_weather(city="Antwerpen"):
    request_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric"

    data = requests.get(request_url).json()

    return data

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name:")

    # Check for empty strings or string with only spaces
    if not bool(city.strip()):       # strip() strips aways spaces
        city = "Antwerpen"

    data = get_current_weather(city)



    #print("\n")
    #pprint(data)