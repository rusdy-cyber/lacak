import requests

def get_location_by_phone_number(phone_number):
    # Masukkan kunci API Google Maps Geolocation Anda di sini
    api_key = "YOUR_API_KEY"

    # URL untuk meminta lokasi berdasarkan nomor telepon
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}"

    # Data yang akan dikirim ke API, termasuk nomor telepon
    data = {
        "considerIp": "false",
        "wifiAccessPoints": [],
        "cellTowers": [
            {
                "cellId": 123456,  # ID tower seluler
                "locationAreaCode": 456,  # Kode area lokasi
                "mobileCountryCode": 360,  # Kode negara seluler
                "mobileNetworkCode": 1,  # Kode jaringan seluler
                "age": 0,
                "signalStrength": -60,  # Kekuatan sinyal
                "timingAdvance": 15  # Kemajuan waktu
            }
        ]
    }

    # Mengirim permintaan POST ke API
    response = requests.post(url, json=data)

    # Memeriksa apakah permintaan berhasil
    if response.status_code == 200:
        location = response.json()["location"]
        return location
    else:
        return None

# Contoh penggunaan
phone_number = "081234567890"
location = get_location_by_phone_number(phone_number)
if location:
    print(f"Lokasi perangkat dengan nomor {phone_number}: {location}")
else:
    print("Tidak dapat melacak lokasi perangkat.")