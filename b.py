import requests

def show_position(latitude, longitude, api_key):
    location = get_location_from_coordinates(latitude, longitude, api_key)
    if location:
        print("Lokasi Anda:")
        print("Negara:", location['country'])
        print("Provinsi:", location['province'])
        print("Kota:", location['city'])
        print("Kabupaten/Kota:", location['district'])
    else:
        print("Gagal melacak lokasi.")

# Fungsi ini hanya digunakan sebagai contoh dan perlu diimplementasikan sesuai dengan kebutuhan Anda.
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

# Contoh penggunaan (harus mengganti nilai-nilai ini sesuai dengan kebutuhan Anda)
api_key = "AIzaSyC-yS1GkdRa9H_0kV96nlmMeJRTK72jOhs"
latitude = 37.7749  # Contoh nilai latitude
longitude = -122.4194  # Contoh nilai longitude

show_position(latitude, longitude, api_key)
