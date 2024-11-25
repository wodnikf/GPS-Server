# GPS-Server
 
Repo contains 2 python script that allows to send data (like latitude, longtitude, altitude, speed_khm) from ADAFRUIT ULTIMATE GPS 4279 to the database that is on webserver.

File flask_app.py should be placed on the server, remember to change something there. For example name of the database, user name and password to database.

File gps_to_server.py can be placed on computer/rasbery pi where GPS is connected to via USB-C. Remember to change IP address, name of database and probably uart, where is connected the usb. You can find by enter this commands in terminal:

```bash
lsusb   // it checks if your computer sees the GPS

ls /dev/tty.*    // To check which serial devices are available on your     system.
```

then pick the right output to use GPS.


The GPS should fix automaticly after connecting to the computer after couple seconds. 

And pls, check if you have the drivers :)
I used CP210x Macintosh OS VCP Driver 6.0.2     - October 26, 2021 
From Silicon Laboratories Inc.
