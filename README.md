# Adaptive Communication Framework for Small Satellites with Secure Cloud Integration
 A MicroPython-based IoT project using ESP32, DHT11, and MQ135 to monitor temperature, humidity, and air quality with real-time Telegram alerts.

🌍 ESP32 Environmental Monitoring System with Telegram Alerts

This project uses an ESP32, DHT11 temperature & humidity sensor, and MQ135 gas sensor to continuously monitor environmental conditions and send **real-time alerts to Telegram** when threshold values are exceeded.

It is ideal for:

* Smart home monitoring
* Indoor air quality monitoring
* Labs & server rooms
* IoT learning projects

🔧 Hardware Components

* ESP32 Development Board
* DHT11 Temperature & Humidity Sensor
* MQ135 Gas Sensor
* Breadboard & Jumper Wires
* WiFi connection

🔌 Pin Connections

| Component        | ESP32 Pin                 |
| ---------------- | ------------------------- |
| DHT11 Data       | GPIO14                    |
| MQ135 Analog Out | GPIO34                    |
| VCC              | 3.3V / 5V (as per sensor) |
| GND              | GND                       |

> ⚠ Ensure MQ135 analog output does **not exceed 3.3V** for ESP32 ADC safety.

📲 Features

* 📡 WiFi connectivity
* 🌡 Temperature monitoring
* 💧 Humidity monitoring
* ⚠ Gas / air quality detection
* 📩 Telegram alert notifications
* 🔁 Auto-reset alerts when values return to normal

⚙️ Threshold Values (Customizable)

```python
TEMP_THRESHOLD = 35     # Celsius
HUM_THRESHOLD = 70      # Percentage
MQ135_THRESHOLD = 1200  # ADC value (0–4095)
```

🤖 Telegram Bot Setup

1. Open Telegram and search for **@BotFather**
2. Create a new bot using `/newbot`
3. Copy the **Bot Token**
4. Get your **Chat ID** using @userinfobot or similar bots
5. Update these values in the code:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = YOUR_CHAT_ID
```

🌐 WiFi Configuration

Update your WiFi credentials in the code:

```python
SSID = "YOUR_WIFI_NAME"
PASSWORD = "YOUR_WIFI_PASSWORD"
```

🧠 Working Principle

1. ESP32 connects to WiFi
2. Reads temperature & humidity from DHT11
3. Reads gas level from MQ135
4. Compares readings with predefined thresholds
5. Sends Telegram alerts when limits are crossed
6. Sends a "back to normal" message once values stabilize

🛠 Software Requirements

* MicroPython firmware for ESP32
* Thonny / uPyCraft / VS Code (with MicroPython extension)
* Required libraries:

  * `network`
  * `urequests`
  * `dht`
  * `machine`

🚀 How to Run

1. Flash MicroPython on ESP32
2. Upload the Python script
3. Update WiFi & Telegram credentials
4. Open Serial Monitor
5. Power the ESP32
6. Receive alerts on Telegram 

📌 Notes

* MQ135 readings vary with environment – calibration recommended
* DHT11 has slower response; wait ~2 seconds between reads
* Internet connection required for Telegram alerts

📜 License

This project is open-source and free to use for **learning and academic purposes**.

👨‍💻 Author

Sai Kiran J
Vishwas V
Vaishanavi V
Electronics & Communication Engineering
ESP32 | IoT | Embedded Systems

---

⭐ If you find this project helpful, don’t forget to star the repository!
