import time
import adafruit_gps
import serial
import requests


uart = serial.Serial("/dev/tty.SLAB_USBtoUART", baudrate=9600, timeout=10) # Probably here you should change also /dev/tty.SLAB_USBtoUART to /dev/tty.{SOMETHING}
gps = adafruit_gps.GPS(uart, debug=False)


gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")


server_url = "http://{server_ip}:5000/NAME OF DATABASE"


last_print = time.monotonic()
while True:
    gps.update()
    current = time.monotonic()
    if current - last_print >= 1.0:
        last_print = current
        if not gps.has_fix:
            print("Waiting for fix...")
            continue

        data = {
            "timestamp": "{}/{}/{} {:02}:{:02}:{:02}".format(
                gps.timestamp_utc.tm_mon,
                gps.timestamp_utc.tm_mday,
                gps.timestamp_utc.tm_year,
                gps.timestamp_utc.tm_hour,
                gps.timestamp_utc.tm_min,
                gps.timestamp_utc.tm_sec,
            ),
            "latitude": gps.latitude,
            "longitude": gps.longitude,
            "altitude": gps.altitude_m,
            "satellites": gps.satellites,
            "speed_kmh": gps.speed_kmh,
            "fix_quality": gps.fix_quality,
        }

        print("=" * 40)
        print(f"Data to send: {data}")

        try:
            response = requests.post(server_url, json=data)
            print(f"Server response: {response.status_code}, {response.text}")
        except Exception as e:
            print(f"Error sending data: {e}")
