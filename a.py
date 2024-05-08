import requests

def get_location_from_phone_number(phone_number, api_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={phone_number}&key={api_key}"
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
api_key = "AIzaSyDSlpanG00Fqrz-gWbieAoMOC5fOY3N2Yg"

phone_number = input("Masukkan nomor telepon Indonesia (contoh: +62811234567): ")

location = get_location_from_phone_number(phone_number, api_key)
if location:
    print(f"\nLokasi nomor telepon {phone_number}:")
    print(f"Negara: {location['country']}")
    print(f"Provinsi: {location['province']}")
    print(f"Kota: {location['city']}")
    print(f"Kabupaten/Kota: {location['district']}")
else:
    print("Gagal melacak lokasi nomor telepon.")