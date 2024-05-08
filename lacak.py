import requests

def get_provinces(api_key):
    url = f"https://api.goapi.io/regional/provinsi?api_key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        provinces = data["data"]
        return provinces
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def get_cities(api_key, province_code):
    url = f"https://api.goapi.io/regional/kota?api_key={api_key}&provinsi={province_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        cities = data["data"]
        return cities
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def get_districts(api_key, city_code):
    url = f"https://api.goapi.io/regional/kecamatan?api_key={api_key}&kota={city_code}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        districts = data["data"]
        return districts
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Contoh penggunaan
api_key = "AIzaSyDAyFihZxk6xl0U6GA_XGb3YmoXB_mg37U"

# Mendapatkan daftar provinsi
provinces = get_provinces(api_key)
if provinces:
    print("Daftar Provinsi:")
    for province in provinces:
        print(f"{province['id']} - {province['nama']}")

# Mendapatkan daftar kota di provinsi tertentu
province_code = "32"  # Kode provinsi Jawa Barat
cities = get_cities(api_key, province_code)
if cities:
    print(f"\nDaftar Kota di Provinsi {province_code}:")
    for city in cities:
        print(f"{city['id']} - {city['nama']}")

# Mendapatkan daftar kecamatan di kota tertentu
city_code = "3276"  # Kode kota Bandung
districts = get_districts(api_key, city_code)
if districts:
    print(f"\nDaftar Kecamatan di Kota {city_code}:")
    for district in districts:
        print(f"{district['id']} - {district['nama']}")
