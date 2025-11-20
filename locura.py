import bluetooth # type: ignore
import time
TARGET_NAME

while True:
    print("Escaneando dispositivos...")
    nearby_devices = bluetooth.discover_devices(duration=5, lookup_names=True)
    for addr, name in nearby_devices:
        if TARGET_NAME.lower() in name.lower():
            print(f"[+] Encontrado: {name} - {addr}")
            print("Si no está en uso, intenta emparejarlo desde la configuración de Windows ahora.")
    time.sleep(10)
