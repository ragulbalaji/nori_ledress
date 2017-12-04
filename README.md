# nori_ledress
Nori's LEDress Prom 2k17, related to LighTIE 16

# Setup
- Setup WiFi Tethering on your phone
- Flash ESP8266 with micropython firmware, methods different for each type of board
- enable `import webrepl_setup`
- open boot.py, uncomment WiFi Config and fill in passwords.
- upload the boot.py & main.py in the ESPMicropython folder
- ws2812b data line on pin15
- ws2812b to +5v USB , GND (ground before connecting anything else)
- ???
- Have a sample app on thunkable.
- PROFIT?

# HTTP Methods
- GET /TEST
	- random color on 2nd Neopixel
- GET /CLEAR
	- Clear strip
- GET /FILL#hex
	- fills strip with hex color

elea(nori) & ragulbalaji 2017