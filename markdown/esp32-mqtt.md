---
title: ESP32 – mqtt
category: Počítače
tags: [linux, mikrokontrolery, espressif]
last_update: 2025-07-09
---


```markdown
# ☁️ ESP32 – MQTT klient pomocí ESP-IDF

Ukázka, jak vytvořit jednoduchého MQTT klienta na ESP32 pomocí knihovny z ESP-IDF.

---

## 📦 Použitý příklad

Espressif poskytuje oficiální ukázku MQTT klienta:

```bash
cd ~/esp
cp -r $IDF_PATH/examples/protocols/mqtt/tcp mqtt_client
cd mqtt_client
```

---

## ⚙️ Nastavení MQTT serveru (brokeru)

```bash
idf.py menuconfig
```

1. Přejdi do:
   - `Example Configuration`
2. Změň:
   - *Broker URI* – např. `mqtt://broker.hivemq.com`
   - Nebo vlastní: `mqtt://192.168.0.10:1883`

---

## 🧪 Kompilace a nahrání

```bash
idf.py set-target esp32
idf.py build
idf.py -p /dev/ttyUSB0 flash monitor
```

---

## 📋 Výstup

Po připojení k MQTT brokeru:

```
I (3519) MQTT_CLIENT: MQTT_EVENT_CONNECTED
I (3529) MQTT_CLIENT: sent publish successful, msg_id=1234
```

---

## 🧠 MQTT struktura (v kódu)

Typický handler v `mqtt_client_main.c`:

```c
esp_mqtt_client_handle_t client = esp_mqtt_client_init(&mqtt_cfg);
esp_mqtt_client_start(client);
esp_mqtt_client_subscribe(client, "/esp32/topic", 0);
esp_mqtt_client_publish(client, "/esp32/topic", "Hello MQTT", 0, 1, 0);
```

---

## 🔐 Podpora TLS

V `menuconfig` můžeš zapnout:
- `Enable SSL support`
- `Broker URI` pak nastav na `mqtts://...`

---

## 📌 Tipy

- Pro testování můžeš použít:
  - MQTT.fx
  - mosquitto_sub/pub
  - webový nástroj: https://mqtt-explorer.com
```
