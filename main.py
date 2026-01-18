import network
import urequests
import time
from machine import Pin, ADC
import dht

# ----------- WiFi Settings -----------
SSID = "YOUR_WIFI_NAME"          # Replace with your WiFi SSID
PASSWORD = "YOUR_WIFI_PASSWORD"  # Replace with your WiFi password

# ----------- Telegram Settings -----------
BOT_TOKEN = "YOUR_BOT_TOKEN"     # Replace with your Telegram Bot Token
CHAT_ID = 123456789              # Replace with your Telegram Chat ID (integer)

# ----------- Sensor Pins -----------
DHT_PIN = 14           # GPIO14 for DHT11
MQ135_PIN = 34         # ADC pin for MQ135

# ----------- Threshold Values -----------
TEMP_THRESHOLD = 35     # Celsius
HUM_THRESHOLD = 70      # Percent
MQ135_THRESHOLD = 1200  # ADC value (0-4095)

# Initialize sensors
dht_sensor = dht.DHT11(Pin(DHT_PIN))
mq135 = ADC(Pin(MQ135_PIN))
mq135.atten(ADC.ATTN_11DB)  # Full range 0–3.6V

# Alert flags
temp_alert_sent = False
hum_alert_sent = False
gas_alert_sent = False

# ----------- Connect to WiFi -----------
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

print("Connecting to WiFi...")
while not wlan.isconnected():
    time.sleep(1)

print("WiFi Connected:", wlan.ifconfig())

# ----------- Telegram Alert Function -----------
def alert(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    try:
        r = urequests.get(url)
        print("Telegram response:", r.text)
        r.close()
    except Exception as e:
        print("Telegram error:", e)

# ----------- Main Loop -----------
while True:
    try:
        # Read DHT11
        dht_sensor.measure()
        temp = dht_sensor.temperature()
        hum = dht_sensor.humidity()

        # Read MQ135
        gas = mq135.read()

        print(f"[{time.time()}] Temp:{temp}C Hum:{hum}% MQ135:{gas}")

        # ----- Temperature Alert -----
        if temp > TEMP_THRESHOLD and not temp_alert_sent:
            alert(f"Temp Alert! {temp}°C exceeded {TEMP_THRESHOLD}°C")
            temp_alert_sent = True
        elif temp <= TEMP_THRESHOLD and temp_alert_sent:
            alert(f"Temp back to normal: {temp}°C")
            temp_alert_sent = False

        # ----- Humidity Alert -----
        if hum > HUM_THRESHOLD and not hum_alert_sent:
            alert(f"Humidity Alert! {hum}% exceeded {HUM_THRESHOLD}%")
            hum_alert_sent = True
        elif hum <= HUM_THRESHOLD and hum_alert_sent:
            alert(f"Humidity back to normal: {hum}%")
            hum_alert_sent = False

        # ----- Gas Alert -----
        if gas > MQ135_THRESHOLD and not gas_alert_sent:
            alert(f"Gas Alert! MQ135 ADC={gas} exceeded {MQ135_THRESHOLD}")
            gas_alert_sent = True
        elif gas <= MQ135_THRESHOLD and gas_alert_sent:
            alert(f"Gas level back to normal: MQ135 ADC={gas}")
            gas_alert_sent = False

        time.sleep(10)  # Delay between readings

    except Exception as e:
        print("Error reading sensors:", e)
        time.sleep(5)
