import requests
import json

def get_location_from_coordinates(latitude, longitude, api_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "OK":
            location_data = data["results"][0]["address_components"]
            location = {
                "country": None,
                "province": None,
                "city": None,
                "district": None
            }
            
            for component in location_data:
                if "country" in component["types"]:
                    location["country"] = component["long_name"]
                elif "administrative_area_level_1" in component["types"]:
                    location["province"] = component["long_name"]
                elif "administrative_area_level_2" in component["types"]:
                    location["city"] = component["long_name"]
                elif "administrative_area_level_3" in component["types"]:
                    location["district"] = component["long_name"]
            
            return location
        else:
            print(f"Error: {data['status']}")
            return None
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Contoh penggunaan
api_key = "AIzaSyC-yS1GkdRa9H_0kV96nlmMeJRTK72jOhs"

def get_user_location():
    if "geolocation" in navigator:
        navigator.geolocation.getCurrentPosition(showPosition);
    else {
        alert("Geolocation is not supported by this browser.");
    }
    
def showPosition(position) {
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;
    location = get_location_from_coordinates(latitude, longitude, api_key)
    if location:
        console.log("Lokasi Anda:")
        console.log("Negara:", location['country'])
        console.log("Provinsi:", location['province'])
        console.log("Kota:", location['city'])
        console.log("Kabupaten/Kota:", location['district'])
    else:
        console.log("Gagal melacak lokasi.")
}

# Panggil fungsi untuk mendapatkan lokasi pengguna
get_user_location()
