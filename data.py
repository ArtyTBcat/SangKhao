import requests, json, time, os

# This file scrape data from the internet or extract data from existing menu

class getdata:
    def __init__(self):
        self.GOOGLE_API_KEY: str = "AIzaSyArRwGP7OCTkPDkBvt_xyMoESjPgmPm0-4"

    def openStreetMap_get_locations(self):
        # Example search for restaurants in a specific location
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": "restaurant",
            "format": "json",
            "addressdetails": "Si Racha, Chao Phraya Surasak, Chon Buri Province, 20110, Thailand",
        }

        response = requests.get(url, params=params)
        data = json.loads(response.text)
        for result in data:
            name = result["display_name"]
            latitude = result["lat"]
            longitude = result["lon"]
            address = result["address"]
            print(f'{name}{latitude}{longitude}{address}')

    def places_API(self, coordinates: list, radius: int = 5000):
        import os
        keywords = ['restaurant']
        radius = f'{radius}'
        for coordinate in coordinates:
            for keyword in keywords:
                if str(f'places{coordinate}.json') not in os.listdir("data/"):
                    print("Warn : Sending Request to google API")
                    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + coordinate + '&radius=' + str(
                        radius) + '&keyword=' + str(keyword) + '&key=' + str(self.GOOGLE_API_KEY)
                    print(url)
                    response = requests.get(url)
                    jj = json.loads(response.text)
                    print(jj)
                    if jj["status"] == "OK":
                        print("STAT : OK")
                        with open(f"data/places{coordinate}.json", "w") as outfile:
                            outfile.write(response.text)
                    else: print("Unable to retrieve data")
                else: print(f"{'': <10}coordinates is satisfied: 'no need to download'")


class learn:
    # import tensorflow as tf
    pass